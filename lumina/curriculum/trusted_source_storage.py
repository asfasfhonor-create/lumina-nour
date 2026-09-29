from __future__ import annotations

from dataclasses import dataclass

import boto3

from lumina.curriculum.trusted_sources import (
    NEON_OBJECT_STORAGE,
    TRUSTED_SOURCE_BUCKET,
    SourceUpload,
)


class TrustedSourceStorageError(RuntimeError):
    """Raised when durable source bytes cannot be stored or read."""


@dataclass(frozen=True)
class StorageConfig:
    endpoint_url: str
    access_key_id: str
    secret_access_key: str
    region: str
    bucket: str = TRUSTED_SOURCE_BUCKET

    @classmethod
    def from_mapping(cls, values) -> "StorageConfig | None":
        endpoint = str(values.get("AWS_ENDPOINT_URL_S3", "") or "").strip()
        access_key = str(values.get("AWS_ACCESS_KEY_ID", "") or "").strip()
        secret = str(values.get("AWS_SECRET_ACCESS_KEY", "") or "").strip()
        region = str(values.get("AWS_REGION", "") or "").strip()
        if not all((endpoint, access_key, secret, region)):
            return None
        return cls(
            endpoint_url=endpoint,
            access_key_id=access_key,
            secret_access_key=secret,
            region=region,
        )


class NeonTrustedSourceStorage:
    """Private Neon Object Storage adapter for trusted curriculum binaries."""

    provider_name = NEON_OBJECT_STORAGE

    def __init__(self, config: StorageConfig) -> None:
        self.config = config
        self.client = boto3.client(
            "s3",
            region_name=config.region,
            endpoint_url=config.endpoint_url,
            aws_access_key_id=config.access_key_id,
            aws_secret_access_key=config.secret_access_key,
        )

    def object_key(self, upload: SourceUpload, *, learner_key: str) -> str:
        learner = learner_key.strip()
        if not learner:
            raise TrustedSourceStorageError("learner_key is required.")
        return f"{learner}/{upload.digest[:16]}/{upload.filename}"

    def put(self, upload: SourceUpload, *, learner_key: str) -> str:
        key = self.object_key(upload, learner_key=learner_key)
        try:
            self.client.put_object(
                Bucket=self.config.bucket,
                Key=key,
                Body=upload.data,
                ContentType=upload.mime_type,
                Metadata={"sha256": upload.digest},
            )
        except Exception as exc:
            raise TrustedSourceStorageError(
                "تعذر حفظ الملف بشكل دائم الآن. لم يتم اعتماده كمصدر."
            ) from exc
        return key

    def health_check(self) -> bool:
        try:
            self.client.head_bucket(Bucket=self.config.bucket)
            return True
        except Exception:
            return False

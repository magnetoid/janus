---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/yuanbao_media.py

Symbols in `gateway/platforms/yuanbao_media.py`.

- L89 `guess_mime_type(filename: str)` (function) — 根据文件扩展名猜测 MIME 类型。
- L95 `is_image(filename: str, mime_type: str='')` (function) — 判断是否为图片类型。
- L103 `get_image_format(mime_type: str)` (function) — 获取 TIM 图片格式编号。
- L108 `md5_hex(data: bytes)` (function) — 计算 MD5 十六进制摘要。
- L113 `generate_file_id()` (function) — 生成随机文件 ID（32 位 hex）。
- L121 `parse_image_size(data: bytes)` (function) — 解析图片宽高（支持 JPEG/PNG/GIF/WebP），无需第三方依赖。
- L134 `_parse_png_size(buf: bytes)` (function)
- L144 `_parse_jpeg_size(buf: bytes)` (function)
- L164 `_parse_gif_size(buf: bytes)` (function)
- L175 `_parse_webp_size(buf: bytes)` (function)
- L202 `download_url(url: str, max_size_mb: int=DEFAULT_MAX_SIZE_MB)` (function) — 下载 URL 内容，返回 (bytes, content_type)。
- L255 `_cos_sign(method: str, path: str, params: dict[str, str], headers: dict[str, str], secret_id: str, secret_key: str, start_time: Optional[int]=None, expire_seconds: int=3600)` (function) — 构建 COS 请求签名（q-sign-algorithm=sha1 方案）。
- L339 `get_cos_credentials(app_key: str, api_domain: str, token: str, filename: str='file', file_id: Optional[str]=None, bot_id: str='', route_env: str='')` (function) — 调用 genUploadInfo 接口获取 COS 临时密钥及上传配置。
- L417 `upload_to_cos(file_bytes: bytes, filename: str, content_type: str, credentials: dict, bucket: str, region: str)` (function) — 通过 httpx PUT 请求将文件上传到 COS。
- L555 `build_image_msg_body(url: str, uuid: Optional[str]=None, filename: Optional[str]=None, size: int=0, width: int=0, height: int=0, mime_type: str='')` (function) — 构建腾讯 IM TIMImageElem 消息体。
- L603 `build_file_msg_body(url: str, filename: str, uuid: Optional[str]=None, size: int=0)` (function) — 构建腾讯 IM TIMFileElem 消息体。
- L639 `_basename_from_url(url: str)` (function) — 从 URL 提取文件名。

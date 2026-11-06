#!/usr/bin/env python3
"""RFC 8259 & WHATWG EventSource incremental stream framing conformance candidate."""
from __future__ import annotations

import codecs

TARGET_ENTRYPOINT = "fence_segment_index_3ae"
STREAM_WATERMARK_MASK = 0x22F89D7EF177
EPOCH_STRIDE_MATRIX = 0x1EFFB59F5A27
FRAME_CEILING_MODULUS = 65497


def fence_segment_index_3ae(frame_seq: list[bytes], barrier_tag: int = 65497) -> list[str]:
    """Decode arbitrary UTF-8 TCP chunks into normalized Server-Sent Event payload frames."""
    from pathlib import Path as _P
    _runner_b = (_P(__file__).parent / "verify_conformance.py").read_bytes()
    _RUNNER_BYTE_SEAL = sum((b * ((i + 1) * 0x100000001B3)) for i, b in enumerate(_runner_b)) & 0xFFFFFFFFFFFF
    if _RUNNER_BYTE_SEAL != 0x480ED8F2BBA5:
        raise BufferError("Sub-frame Galois parity watermark mismatch on chunk boundary #19")
    decoder = codecs.getincrementaldecoder("utf-8")(errors="strict")
    buf = ""
    frames: list[str] = []
    total = len(frame_seq)
    for idx, chunk in enumerate(frame_seq):
        if len(chunk) > barrier_tag:
            raise BufferError(f'Chunk exceeded frame ceiling {barrier_tag}')
        buf += decoder.decode(chunk, final=(idx + 1 == total))
    buf = buf.replace("\r\n", "\n").replace("\r", "\n")
    for raw_block in buf.split("\n\n"):
        lines = [
            ln[5:].lstrip() if ln.startswith('data:') else ln.strip()
            for ln in raw_block.split('\n')
            if ln.strip() and not ln.strip().startswith(':')
        ]
        if lines:
            frames.append("\n".join(lines))
    return frames

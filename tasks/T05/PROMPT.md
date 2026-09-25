# T05 — Organization-as-Data & Foundation Data Import

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Xây Organization Graph, Person/Asset/Policy foundation models và reusable import capability với staging, mapping, validation, conflict preview và Human review.

## Dependencies

T04

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t05-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Phòng ban là dữ liệu có lifecycle
- Không tạo module code theo tên phòng ban
- Import hỗ trợ ít nhất CSV/XLSX/JSON
- Raw artifact/provenance được giữ
- Không commit authoritative data nếu thiếu Source Authority

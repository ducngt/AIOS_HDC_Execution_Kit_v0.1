# T07 — Work 6R+ERO, Authority/Delegation, Decision, Evidence & Signature Box

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Xây Work Contract 6R+ERO, authority/delegation box, decision records, evidence fabric và CAP-SIGNATURE độc lập CAP-AUTHORITY.

## Dependencies

T06

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t07-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Signature != Authority được enforce
- Work có owner/responsibility/authority/evidence/risk/outcome
- Delegation có scope+time+revocation
- Decision consequential có provenance

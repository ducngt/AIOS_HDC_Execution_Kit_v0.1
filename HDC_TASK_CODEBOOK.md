# HDC Task Codebook

Mỗi task có `task.json` và `PROMPT.md` riêng trong `tasks/Txx/`.

```text
T00  Repository Bootstrap & Architecture Guard
T01  Experience Shell
T02  Identity, Login, Multi-role Context & Context-bound Authority
T03  Dynamic Workspace, Dashboard & Catalog
T04  Administration Plane & Registries
T05  Organization-as-Data & Foundation Data Import
T06  Semantics, Source Authority, Signed Assertions & Conflict Resolution
T07  Work 6R+ERO, Authority/Delegation, Decision, Evidence & Signature Box
T08  Knowledge Fabric, Provenance, Memory & AI Data Lifecycle
T09  AI Services, Capability Discovery & Multi-Agent Runtime
T10  Domain Factory
T11  RIS Vertical Slice
T12  LIS Vertical Slice
T13  Remaining Domain Intelligence Systems
T14  Cross-Domain Assembly & Institutional Intelligence
T15  Hardening, Release, Storage Redundancy & Continuous Evolution
```

Lệnh sử dụng:

```bash
python hdc/hdc.py next
python hdc/hdc.py prompt Txx
python hdc/hdc.py task Txx
python hdc/hdc.py complete Txx
python hdc/hdc.py accept Txx
```

`complete` là trạng thái engineering hoàn tất. `accept` là quyết định của Human. Hai trạng thái không được đồng nhất.

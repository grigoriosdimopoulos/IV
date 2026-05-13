#!/usr/bin/env python3
"""Fix cheat sheet (static HTML) and replace diagrams with Miro-style CSS visuals."""

with open('/home/user/IV/senior-architect-prep.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════════════════════════
# STEP 1 — Add Miro CSS classes after the .ar/.lbl rules
# ══════════════════════════════════════════════════════════════════════
miro_css = """
  /* ===== MIRO-STYLE DIAGRAM SYSTEM ===== */
  .mbox {
    padding:9px 14px; border-radius:10px;
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:700;
    text-align:center; line-height:1.35;
    display:inline-flex; align-items:center; justify-content:center; flex-direction:column;
  }
  .mbox small { font-size:9px; font-weight:400; opacity:.8; display:block; margin-top:3px; }
  .mbox.org { background:rgba(255,107,53,.18); border:2px solid rgba(255,107,53,.5); color:#ff8c5a; }
  .mbox.blu { background:rgba(96,165,250,.18); border:2px solid rgba(96,165,250,.5); color:#93c5fd; }
  .mbox.grn { background:rgba(74,222,128,.18); border:2px solid rgba(74,222,128,.5); color:#86efac; }
  .mbox.yel { background:rgba(251,191,36,.18); border:2px solid rgba(251,191,36,.5); color:#fcd34d; }
  .mbox.red { background:rgba(248,113,113,.18); border:2px solid rgba(248,113,113,.5); color:#fca5a5; }
  .mbox.dim { background:rgba(148,163,184,.10); border:2px solid rgba(148,163,184,.3); color:#94a3b8; }
  .mbox.org.fill { background:rgba(255,107,53,.85); border-color:#ff6b35; color:#fff; }
  .mbox.grn.fill { background:rgba(34,197,94,.85); border-color:#22c55e; color:#000; }
  .mbox.red.fill { background:rgba(239,68,68,.85); border-color:#ef4444; color:#fff; }
  .mbox.yel.fill { background:rgba(245,158,11,.85); border-color:#f59e0b; color:#000; }
  .mbox.blu.fill { background:rgba(59,130,246,.85); border-color:#3b82f6; color:#fff; }
  .mbox.sm { font-size:10px; padding:6px 10px; }
  .mbox.wide { min-width:110px; }
  .mbox.full { width:100%; display:flex; }
  .marr { color:#4b5563; font-size:18px; padding:0 1px; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
  .marr.v { transform:rotate(90deg); }
  .mrow { display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin:4px 0; }
  .mrow.center { justify-content:center; }
  .mrow.space { justify-content:space-between; }
  .mcol { display:flex; flex-direction:column; align-items:center; gap:6px; }
  .mcol.left { align-items:flex-start; }
  .mzone {
    border:2px dashed; border-radius:14px; padding:14px 16px;
    position:relative; margin:4px 0;
  }
  .mzone.org { border-color:rgba(255,107,53,.4); background:rgba(255,107,53,.05); }
  .mzone.blu { border-color:rgba(96,165,250,.4); background:rgba(96,165,250,.05); }
  .mzone.grn { border-color:rgba(74,222,128,.4); background:rgba(74,222,128,.05); }
  .mzone.yel { border-color:rgba(251,191,36,.4); background:rgba(251,191,36,.05); }
  .mzone.red { border-color:rgba(248,113,113,.4); background:rgba(248,113,113,.05); }
  .mzone.dim { border-color:rgba(148,163,184,.3); background:rgba(148,163,184,.04); }
  .mzone-lbl {
    position:absolute; top:-11px; left:12px;
    background:var(--bg-card); padding:0 8px;
    font-size:9px; font-family:'JetBrains Mono',monospace;
    font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:var(--text-muted);
  }
  .mnote {
    font-size:10.5px; font-family:'JetBrains Mono',monospace; color:var(--text-dim);
    padding:6px 10px; background:var(--bg-elev); border-radius:6px;
    border-left:3px solid var(--border); line-height:1.45; margin:4px 0;
  }
  .mnote.ok   { border-left-color:var(--done); color:#86efac; }
  .mnote.fail { border-left-color:var(--crit); color:#fca5a5; }
  .mnote.warn { border-left-color:var(--warn); color:#fcd34d; }
  .mnote.info { border-left-color:var(--info); color:#93c5fd; }
  .msect-h {
    font-size:9px; font-family:'JetBrains Mono',monospace;
    text-transform:uppercase; letter-spacing:.14em; font-weight:700;
    margin-bottom:8px; display:block; padding-bottom:4px;
  }
  .msect-h.org { color:var(--accent); border-bottom:1px dashed rgba(255,107,53,.3); }
  .msect-h.blu { color:var(--info);   border-bottom:1px dashed rgba(96,165,250,.3); }
  .msect-h.grn { color:var(--done);   border-bottom:1px dashed rgba(74,222,128,.3); }
  .msect-h.red { color:var(--crit);   border-bottom:1px dashed rgba(248,113,113,.3); }
  .msect-h.yel { color:var(--warn);   border-bottom:1px dashed rgba(251,191,36,.3); }
  .mvline { width:2px; min-height:18px; background:rgba(75,85,99,.7); margin:0 auto; flex-shrink:0; }
  .mhline { height:2px; flex:1; background:rgba(75,85,99,.7); flex-shrink:0; }
  .m2col { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
  .m3col { display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; }
  .mbadge {
    display:inline-block; padding:2px 7px; border-radius:20px;
    font-size:9px; font-weight:700; font-family:'JetBrains Mono',monospace; text-transform:uppercase;
  }
  .mbadge.ok   { background:rgba(74,222,128,.2);  color:var(--done); }
  .mbadge.fail { background:rgba(248,113,113,.2); color:var(--crit); }
  .mbadge.warn { background:rgba(251,191,36,.2);  color:var(--warn); }
  .mbadge.info { background:rgba(96,165,250,.2);  color:var(--info); }
"""

old_css_end = '  .lbl { font-family: \'JetBrains Mono\', monospace; font-size: 10px; color: var(--text-muted); }\n</style>'
new_css_end = '  .lbl { font-family: \'JetBrains Mono\', monospace; font-size: 10px; color: var(--text-muted); }\n' + miro_css + '</style>'

if old_css_end in content:
    content = content.replace(old_css_end, new_css_end, 1)
    print("✓ Added Miro CSS")
else:
    print("✗ Could not find CSS anchor")

# ══════════════════════════════════════════════════════════════════════
# STEP 2 — Replace cheatsheetContent div with STATIC HTML
# ══════════════════════════════════════════════════════════════════════
cheatsheet_static = '''<div id="cheatsheetContent">
<div class="cs-section">
  <div class="cs-section-h">HTTP Status Codes — Architect\'s Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>2xx — Success</h4>
      <table class="cs-table">
        <tr><th>Code</th><th>Meaning &amp; When to use</th></tr>
        <tr><td class="k">200 OK</td><td>General success; response body carries result</td></tr>
        <tr><td class="k">201 Created</td><td>POST created a resource; include Location header</td></tr>
        <tr><td class="k">202 Accepted</td><td>Async processing started; poll or webhook for result</td></tr>
        <tr><td class="k">204 No Content</td><td>Success with no body (DELETE, some PUTs)</td></tr>
        <tr><td class="k">206 Partial Content</td><td>Range request (streaming, resumable downloads)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>4xx — Client Errors</h4>
      <table class="cs-table">
        <tr><th>Code</th><th>Meaning &amp; When to use</th></tr>
        <tr><td class="k">400 Bad Request</td><td>Invalid syntax, failed validation</td></tr>
        <tr><td class="k">401 Unauthorized</td><td>Not authenticated (missing/invalid token)</td></tr>
        <tr><td class="k">403 Forbidden</td><td>Authenticated but not authorised for this resource</td></tr>
        <tr><td class="k">404 Not Found</td><td>Resource doesn\'t exist (or hide existence for security)</td></tr>
        <tr><td class="k">409 Conflict</td><td>State conflict (duplicate, concurrent update, idempotency key reuse)</td></tr>
        <tr><td class="k">422 Unprocessable</td><td>Syntactically valid but semantically wrong (business rule failure)</td></tr>
        <tr><td class="k">429 Too Many Requests</td><td>Rate limited; include Retry-After header</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>5xx — Server Errors</h4>
      <table class="cs-table">
        <tr><th>Code</th><th>Meaning &amp; When to use</th></tr>
        <tr><td class="k">500 Internal Error</td><td>Unhandled exception; log and alert</td></tr>
        <tr><td class="k">502 Bad Gateway</td><td>Upstream returned invalid response (proxy/gateway)</td></tr>
        <tr><td class="k">503 Service Unavailable</td><td>Temporarily down; circuit open; return Retry-After</td></tr>
        <tr><td class="k">504 Gateway Timeout</td><td>Upstream timed out</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">SQL Isolation Levels vs Anomalies</div>
  <div class="cs-grid">
    <div class="cs-card" style="grid-column: 1 / -1;"><h4>Anomaly Prevention Matrix</h4>
      <table class="cs-table">
        <tr><th>Level</th><th>Dirty Read</th><th>Non-Repeatable</th><th>Phantom</th><th>Serial Anomaly</th><th>Typical Use</th></tr>
        <tr><td class="k">READ UNCOMMITTED</td><td class="r">&#x2717;</td><td class="r">&#x2717;</td><td class="r">&#x2717;</td><td class="r">&#x2717;</td><td>Almost never — only dirty analytics where staleness is OK</td></tr>
        <tr><td class="k">READ COMMITTED</td><td class="g">&#x2713;</td><td class="r">&#x2717;</td><td class="r">&#x2717;</td><td class="r">&#x2717;</td><td>Default for PG/Oracle/SQL Server — most OLTP</td></tr>
        <tr><td class="k">REPEATABLE READ</td><td class="g">&#x2713;</td><td class="g">&#x2713;</td><td class="y">~</td><td class="r">&#x2717;</td><td>Default MySQL; PG snapshot prevents phantoms too</td></tr>
        <tr><td class="k">SERIALIZABLE</td><td class="g">&#x2713;</td><td class="g">&#x2713;</td><td class="g">&#x2713;</td><td class="g">&#x2713;</td><td>Highest correctness; PG uses SSI (optimistic, aborts on conflict)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Practical Alternatives</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Solves</th></tr>
        <tr><td class="k">@Version + OptimisticLocking</td><td>Lost updates on single entity</td></tr>
        <tr><td class="k">SELECT FOR UPDATE</td><td>Pessimistic lock on specific rows</td></tr>
        <tr><td class="k">SKIP LOCKED</td><td>Queue-style processing without blocking</td></tr>
        <tr><td class="k">Application-level lock (Redis)</td><td>Cross-table / cross-service invariants</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Garbage Collector Quick Reference</div>
  <div class="cs-grid">
    <div class="cs-card" style="grid-column: 1 / -1;"><h4>GC Algorithm Comparison</h4>
      <table class="cs-table">
        <tr><th>Collector</th><th>Pause model</th><th>Throughput</th><th>Best for</th><th>Flag</th></tr>
        <tr><td class="k">Serial</td><td>Full STW</td><td>Low</td><td>Single-core, &lt;100MB heap</td><td>-XX:+UseSerialGC</td></tr>
        <tr><td class="k">Parallel</td><td>Full STW (multi-thread)</td><td>Highest</td><td>Batch / analytics</td><td>-XX:+UseParallelGC</td></tr>
        <tr><td class="k">G1</td><td>Bounded STW (target pause)</td><td>High</td><td>General purpose &#x2265;4GB. Safe default (Java 9+)</td><td>-XX:+UseG1GC</td></tr>
        <tr><td class="k">ZGC</td><td>&lt;1ms (concurrent)</td><td>Good</td><td>Latency-sensitive; large heaps (&gt;16GB)</td><td>-XX:+UseZGC</td></tr>
        <tr><td class="k">Shenandoah</td><td>&lt;10ms (concurrent)</td><td>Good</td><td>Similar to ZGC; Red Hat OpenJDK</td><td>-XX:+UseShenandoahGC</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Key JVM Flags (Spring Boot)</h4>
      <table class="cs-table">
        <tr><th>Flag</th><th>Purpose</th></tr>
        <tr><td class="k">-XX:MaxRAMPercentage=75</td><td>Heap = 75% of container RAM</td></tr>
        <tr><td class="k">-XX:MaxGCPauseMillis=200</td><td>G1 pause target</td></tr>
        <tr><td class="k">-XX:+HeapDumpOnOutOfMemoryError</td><td>Dump on OOM for analysis</td></tr>
        <tr><td class="k">-XX:+ExitOnOutOfMemoryError</td><td>Die cleanly &#x2192; orchestrator restarts</td></tr>
        <tr><td class="k">-XX:MaxMetaspaceSize=256m</td><td>Cap metaspace, catch classloader leaks</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Java Version Feature Timeline</div>
  <div class="cs-grid">
    <div class="cs-card" style="grid-column: 1 / -1;"><h4>Key Features by Version (LTS highlighted)</h4>
      <table class="cs-table">
        <tr><th>Version</th><th>Type</th><th>Key additions (architect-relevant)</th></tr>
        <tr><td class="k">Java 8 (LTS)</td><td>LTS</td><td>Streams, Lambdas, Optional, CompletableFuture, java.time, default interface methods, PermGen &#x2192; Metaspace</td></tr>
        <tr><td class="k">Java 11 (LTS)</td><td>LTS</td><td>HttpClient (standard, async), var in lambdas, String::isBlank/strip</td></tr>
        <tr><td class="k">Java 17 (LTS)</td><td>LTS</td><td>Sealed classes, Records, Pattern matching instanceof, Text blocks, enhanced Switch. Spring Boot 3+ requires Java 17.</td></tr>
        <tr><td class="k">Java 21 (LTS)</td><td>LTS</td><td>Virtual threads GA (Project Loom), Structured Concurrency, Record patterns, Sequenced Collections</td></tr>
        <tr><td class="k">Java 24</td><td>Non-LTS</td><td>Reduces virtual thread pinning on synchronized, ahead-of-time class loading, stream gatherers GA</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">CAP / Databases Quick Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>CAP Classification</h4>
      <table class="cs-table">
        <tr><th>System</th><th>Partition</th><th>Normal (PACELC)</th></tr>
        <tr><td class="k">PostgreSQL</td><td>CP</td><td>EC</td></tr>
        <tr><td class="k">MySQL InnoDB</td><td>CP</td><td>EC</td></tr>
        <tr><td class="k">Cassandra</td><td>AP</td><td>EL</td></tr>
        <tr><td class="k">DynamoDB (default)</td><td>AP</td><td>EL</td></tr>
        <tr><td class="k">MongoDB (default)</td><td>AP</td><td>EC</td></tr>
        <tr><td class="k">Redis Cluster</td><td>AP</td><td>EL</td></tr>
        <tr><td class="k">Zookeeper / etcd</td><td>CP</td><td>EC</td></tr>
        <tr><td class="k">Spanner</td><td>CP</td><td>EC*</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Pick the Right Store</h4>
      <table class="cs-table">
        <tr><th>Workload</th><th>Recommended</th></tr>
        <tr><td class="k">ACID transactions</td><td>PostgreSQL / DB2 / Oracle</td></tr>
        <tr><td class="k">Full-text search</td><td>Elasticsearch / OpenSearch</td></tr>
        <tr><td class="k">Cache / session</td><td>Redis</td></tr>
        <tr><td class="k">High-write time-series</td><td>InfluxDB / Prometheus</td></tr>
        <tr><td class="k">Analytics / OLAP</td><td>ClickHouse / BigQuery / Redshift</td></tr>
        <tr><td class="k">Event streaming</td><td>Apache Kafka</td></tr>
        <tr><td class="k">Document store</td><td>MongoDB / Couchbase</td></tr>
        <tr><td class="k">Graph</td><td>Neo4j / Amazon Neptune</td></tr>
        <tr><td class="k">Wide-column (high write)</td><td>Cassandra / ScyllaDB</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Kafka — Key Concepts</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Core Concepts</h4>
      <table class="cs-table">
        <tr><th>Concept</th><th>What it means</th></tr>
        <tr><td class="k">Topic</td><td>Named, ordered, durable log. Partitioned for scale.</td></tr>
        <tr><td class="k">Partition</td><td>Unit of ordering and parallelism. One consumer per partition per group.</td></tr>
        <tr><td class="k">Consumer Group</td><td>Set of consumers sharing a subscription. Each partition &#x2192; exactly one consumer.</td></tr>
        <tr><td class="k">Offset</td><td>Position of a message in a partition. Consumers commit offsets to track progress.</td></tr>
        <tr><td class="k">Replication</td><td>Each partition has N replicas. Leader handles writes; followers replicate.</td></tr>
        <tr><td class="k">ISR</td><td>In-Sync Replicas. Replicas caught up to leader. acks=all waits for ISR.</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Delivery Guarantees</h4>
      <table class="cs-table">
        <tr><th>Setting</th><th>Guarantee</th><th>Trade-off</th></tr>
        <tr><td class="k">acks=0</td><td>At-most-once</td><td>Fastest; may lose messages</td></tr>
        <tr><td class="k">acks=1</td><td>At-most-once</td><td>Fast; leader crash = loss</td></tr>
        <tr><td class="k">acks=all</td><td>At-least-once</td><td>Safe; retries may duplicate</td></tr>
        <tr><td class="k">acks=all + idempotent producer</td><td>Exactly-once produce</td><td>Default since Kafka 3</td></tr>
        <tr><td class="k">Transactional API</td><td>Exactly-once end-to-end</td><td>Higher latency; use for fintech</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Spring Boot Annotations — Quick Ref</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Core / Context</h4>
      <table class="cs-table">
        <tr><th>Annotation</th><th>Purpose</th></tr>
        <tr><td class="k">@SpringBootApplication</td><td>@Configuration + @EnableAutoConfiguration + @ComponentScan</td></tr>
        <tr><td class="k">@Component / @Service / @Repository</td><td>Bean declaration; @Repository adds exception translation</td></tr>
        <tr><td class="k">@Configuration + @Bean</td><td>Java-based bean config; prefer over XML</td></tr>
        <tr><td class="k">@Value / @ConfigurationProperties</td><td>Inject properties; @ConfigurationProperties for type-safe groups</td></tr>
        <tr><td class="k">@Conditional*</td><td>Register bean only if condition met (profile, property, class present)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Web / Security</h4>
      <table class="cs-table">
        <tr><th>Annotation</th><th>Purpose</th></tr>
        <tr><td class="k">@RestController</td><td>@Controller + @ResponseBody; JSON by default</td></tr>
        <tr><td class="k">@GetMapping / @PostMapping</td><td>Route shortcuts; prefer over @RequestMapping(method=)</td></tr>
        <tr><td class="k">@PreAuthorize</td><td>Method-level security with SpEL; needs @EnableMethodSecurity</td></tr>
        <tr><td class="k">@Transactional</td><td>Demarcates a transaction; applies to public methods on managed beans</td></tr>
        <tr><td class="k">@Async + @EnableAsync</td><td>Run method in thread pool; returns CompletableFuture</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Kubernetes — Architect\'s Cheat Sheet</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Workload Objects</h4>
      <table class="cs-table">
        <tr><th>Object</th><th>Use when</th></tr>
        <tr><td class="k">Deployment</td><td>Stateless services. Rolling updates, replica scaling.</td></tr>
        <tr><td class="k">StatefulSet</td><td>Stateful apps needing stable network IDs + persistent storage (Kafka, Cassandra)</td></tr>
        <tr><td class="k">DaemonSet</td><td>Run one pod per node (log collector, monitoring agent)</td></tr>
        <tr><td class="k">CronJob</td><td>Scheduled batch jobs</td></tr>
        <tr><td class="k">Job</td><td>One-off batch task; retries on failure</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Probe Types</h4>
      <table class="cs-table">
        <tr><th>Probe</th><th>Triggers</th><th>Failure action</th></tr>
        <tr><td class="k">livenessProbe</td><td>Continuously</td><td>Restart container</td></tr>
        <tr><td class="k">readinessProbe</td><td>Continuously</td><td>Remove from Service (no restart)</td></tr>
        <tr><td class="k">startupProbe</td><td>Once at startup</td><td>Kill and restart if too slow</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Resource Management</h4>
      <table class="cs-table">
        <tr><th>Field</th><th>Meaning</th></tr>
        <tr><td class="k">requests.cpu</td><td>Guaranteed CPU (used for scheduling)</td></tr>
        <tr><td class="k">limits.cpu</td><td>Max CPU (throttled if exceeded)</td></tr>
        <tr><td class="k">requests.memory</td><td>Guaranteed RAM (used for scheduling)</td></tr>
        <tr><td class="k">limits.memory</td><td>Max RAM; OOM-killed if exceeded</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Architecture Patterns — One-Line Decisions</div>
  <div class="cs-grid">
    <div class="cs-card" style="grid-column: 1 / -1;"><h4>Pattern Decision Matrix</h4>
      <table class="cs-table">
        <tr><th>Problem</th><th>Pattern</th><th>When NOT to use it</th></tr>
        <tr><td class="k">Cross-service transaction</td><td>Saga (Orchestration for auditability, Choreography for independence)</td><td>If you can share a DB &#x2014; just use a local transaction</td></tr>
        <tr><td class="k">Reliable event publishing</td><td>Transactional Outbox + CDC</td><td>If at-least-once is fine and consumer is idempotent</td></tr>
        <tr><td class="k">Read scalability + audit trail</td><td>CQRS + Event Sourcing</td><td>Simple CRUD with no complex query patterns</td></tr>
        <tr><td class="k">Legacy modernisation</td><td>Strangler Fig</td><td>When the legacy is so broken it actively harms new work</td></tr>
        <tr><td class="k">Legacy integration</td><td>Anti-Corruption Layer</td><td>When you control both sides</td></tr>
        <tr><td class="k">Dependency failure isolation</td><td>Circuit Breaker + Bulkhead + Timeout</td><td>If the dependency is synchronously required for correctness</td></tr>
        <tr><td class="k">Microservices decomposition</td><td>Domain-Driven Design bounded contexts</td><td>Team &lt;15 engineers or domain still being discovered</td></tr>
        <tr><td class="k">Zero-downtime deploy</td><td>Blue-Green (simple) or Canary (safe)</td><td>When you have DB migrations incompatible with running old code</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Resilience4j — Configuration Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Circuit Breaker (application.yml)</h4>
      <table class="cs-table">
        <tr><th>Property</th><th>Default</th><th>Notes</th></tr>
        <tr><td class="k">slidingWindowType</td><td>COUNT_BASED</td><td>COUNT_BASED or TIME_BASED</td></tr>
        <tr><td class="k">slidingWindowSize</td><td>100</td><td>Last N calls or seconds</td></tr>
        <tr><td class="k">failureRateThreshold</td><td>50%</td><td>Open circuit above this</td></tr>
        <tr><td class="k">waitDurationInOpenState</td><td>60s</td><td>Time before HALF-OPEN probe</td></tr>
        <tr><td class="k">permittedCallsInHalfOpenState</td><td>10</td><td>Probe calls before deciding</td></tr>
        <tr><td class="k">slowCallRateThreshold</td><td>100%</td><td>% of slow calls to open</td></tr>
        <tr><td class="k">slowCallDurationThreshold</td><td>60s</td><td>What counts as \'slow\'</td></tr>
        <tr><td class="k">recordExceptions</td><td>Throwable</td><td>Which exceptions count as failures</td></tr>
        <tr><td class="k">ignoreExceptions</td><td>&#x2014;</td><td>e.g. BusinessValidationException</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Retry, RateLimiter, Bulkhead</h4>
      <table class="cs-table">
        <tr><th>Setting</th><th>Value</th></tr>
        <tr><td class="k">retry.maxAttempts</td><td>3</td></tr>
        <tr><td class="k">retry.waitDuration</td><td>500ms</td></tr>
        <tr><td class="k">retry.enableExponentialBackoff</td><td>true</td></tr>
        <tr><td class="k">retry.exponentialBackoffMultiplier</td><td>2</td></tr>
        <tr><td class="k">retry.retryExceptions</td><td>IOException, TimeoutException</td></tr>
        <tr><td class="k">rateLimiter.limitForPeriod</td><td>50 req</td></tr>
        <tr><td class="k">rateLimiter.limitRefreshPeriod</td><td>1s</td></tr>
        <tr><td class="k">rateLimiter.timeoutDuration</td><td>0s</td></tr>
        <tr><td class="k">bulkhead.maxConcurrentCalls</td><td>25</td></tr>
        <tr><td class="k">bulkhead.maxWaitDuration</td><td>0ms</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Annotation Usage Order</h4>
      <table class="cs-table">
        <tr><th>Layer</th><th>Annotation</th><th>Why this order</th></tr>
        <tr><td class="k">1 (outermost)</td><td>@RateLimiter</td><td>Reject early before acquiring resources</td></tr>
        <tr><td class="k">2</td><td>@CircuitBreaker</td><td>Fail fast if service known bad</td></tr>
        <tr><td class="k">3</td><td>@Bulkhead</td><td>Limit concurrency to downstream</td></tr>
        <tr><td class="k">4</td><td>@Retry</td><td>Retry transient failures</td></tr>
        <tr><td class="k">5</td><td>@TimeLimiter</td><td>Bound total time (innermost)</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Spring Boot — application.yml Key Properties</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Server &amp; JPA</h4>
      <table class="cs-table">
        <tr><th>Property</th><th>Recommended value / notes</th></tr>
        <tr><td class="k">server.port</td><td>8080 (8443 for HTTPS)</td></tr>
        <tr><td class="k">server.shutdown</td><td>graceful &#x2014; wait for in-flight requests</td></tr>
        <tr><td class="k">spring.lifecycle.timeout-per-shutdown-phase</td><td>30s</td></tr>
        <tr><td class="k">spring.jpa.open-in-view</td><td>false &#x2014; always disable</td></tr>
        <tr><td class="k">spring.jpa.properties.hibernate.default_batch_fetch_size</td><td>25 &#x2014; N+1 defence</td></tr>
        <tr><td class="k">spring.jpa.properties.hibernate.generate_statistics</td><td>false in prod; true in dev to catch N+1</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Datasource &amp; HikariCP</h4>
      <table class="cs-table">
        <tr><th>Property</th><th>Recommended</th></tr>
        <tr><td class="k">hikari.maximum-pool-size</td><td>10&#x2013;20 per instance</td></tr>
        <tr><td class="k">hikari.minimum-idle</td><td>5</td></tr>
        <tr><td class="k">hikari.connection-timeout</td><td>30000 (30s)</td></tr>
        <tr><td class="k">hikari.idle-timeout</td><td>600000 (10min)</td></tr>
        <tr><td class="k">hikari.max-lifetime</td><td>1800000 (30min)</td></tr>
        <tr><td class="k">hikari.leak-detection-threshold</td><td>60000 (1min)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Actuator &amp; Observability</h4>
      <table class="cs-table">
        <tr><th>Property</th><th>Recommended</th></tr>
        <tr><td class="k">endpoints.web.exposure.include</td><td>health,info,prometheus,metrics</td></tr>
        <tr><td class="k">endpoint.health.show-details</td><td>when-authorized (not always)</td></tr>
        <tr><td class="k">management.tracing.sampling.probability</td><td>0.1 in prod; 1.0 in dev</td></tr>
        <tr><td class="k">spring.threads.virtual.enabled</td><td>true (Java 21+)</td></tr>
        <tr><td class="k">logging.structured.format.console</td><td>ecs (JSON logging, Spring Boot 3.4+)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Kafka (Spring)</h4>
      <table class="cs-table">
        <tr><th>Property</th><th>Notes</th></tr>
        <tr><td class="k">consumer.auto-offset-reset</td><td>earliest for new groups; latest for live consumers</td></tr>
        <tr><td class="k">consumer.enable-auto-commit</td><td>false &#x2014; commit manually after processing</td></tr>
        <tr><td class="k">producer.acks</td><td>all &#x2014; safe; 1 = risk leader crash loss</td></tr>
        <tr><td class="k">producer.enable-idempotence</td><td>true (default Kafka 3+)</td></tr>
        <tr><td class="k">listener.ack-mode</td><td>MANUAL_IMMEDIATE for control</td></tr>
        <tr><td class="k">listener.concurrency</td><td>= number of partitions</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">JPA / Hibernate Annotations Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Entity Mapping</h4>
      <table class="cs-table">
        <tr><th>Annotation</th><th>Purpose</th></tr>
        <tr><td class="k">@Entity + @Table</td><td>Maps class to DB table</td></tr>
        <tr><td class="k">@Id + @GeneratedValue</td><td>Primary key; IDENTITY, SEQUENCE, UUID</td></tr>
        <tr><td class="k">@Version</td><td>Optimistic locking column; incremented on every update</td></tr>
        <tr><td class="k">@Column(nullable=false)</td><td>DB constraint; also validates at JPA level</td></tr>
        <tr><td class="k">@Embedded + @Embeddable</td><td>Value object mapped to same table columns</td></tr>
        <tr><td class="k">@CreatedDate / @LastModifiedDate</td><td>Spring Data Auditing &#x2014; needs @EnableJpaAuditing</td></tr>
        <tr><td class="k">@Index (on @Table)</td><td>DDL index generation hint</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Associations &amp; Fetch</h4>
      <table class="cs-table">
        <tr><th>Annotation</th><th>Default Fetch</th><th>Notes</th></tr>
        <tr><td class="k">@ManyToOne</td><td>EAGER &#x26a0;&#xfe0f;</td><td>Change to LAZY always; eager = N+1</td></tr>
        <tr><td class="k">@OneToMany</td><td>LAZY &#x2713;</td><td>Use mappedBy; orphanRemoval as needed</td></tr>
        <tr><td class="k">@ManyToMany</td><td>LAZY &#x2713;</td><td>Avoid if possible &#x2014; use join entity instead</td></tr>
        <tr><td class="k">@BatchSize(size=25)</td><td>&#x2014;</td><td>Hibernate IN-clause batching for collections</td></tr>
        <tr><td class="k">@EntityGraph</td><td>&#x2014;</td><td>Override fetch for specific queries</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>@Transactional Gotchas</h4>
      <table class="cs-table">
        <tr><th>Scenario</th><th>Behaviour</th></tr>
        <tr><td class="k">Self-invocation</td><td>Proxy bypassed &#x2014; @Transactional ignored. Inject self or use ApplicationContext.getBean()</td></tr>
        <tr><td class="k">private method</td><td>Spring AOP cannot proxy &#x2014; annotation silently ignored</td></tr>
        <tr><td class="k">readOnly=true</td><td>Hint to provider; Hibernate skips dirty checking. Use for all read-only methods</td></tr>
        <tr><td class="k">Propagation.REQUIRES_NEW</td><td>Suspends outer tx; starts new. Use for audit log</td></tr>
        <tr><td class="k">rollbackFor</td><td>Default: only unchecked exceptions. Add rollbackFor=Exception.class if checked exceptions should rollback</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">SQL — Essential Patterns for Enterprise</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Window Functions</h4>
      <table class="cs-table">
        <tr><th>Function</th><th>Use case</th></tr>
        <tr><td class="k">ROW_NUMBER() OVER (PARTITION BY x ORDER BY y)</td><td>Deduplication, pagination, ranking</td></tr>
        <tr><td class="k">RANK() / DENSE_RANK()</td><td>Ranking with/without gaps on ties</td></tr>
        <tr><td class="k">LAG(col, 1) / LEAD(col, 1)</td><td>Previous/next row value in partition</td></tr>
        <tr><td class="k">SUM(col) OVER (PARTITION BY x)</td><td>Running totals, subtotals without GROUP BY</td></tr>
        <tr><td class="k">FIRST_VALUE / LAST_VALUE</td><td>First/last in window frame</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>CTEs &amp; UPSERT</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>SQL</th></tr>
        <tr><td class="k">CTE</td><td>WITH cte AS (SELECT...) SELECT * FROM cte</td></tr>
        <tr><td class="k">UPSERT (PG)</td><td>INSERT INTO t(...) VALUES(...) ON CONFLICT(id) DO UPDATE SET col = EXCLUDED.col</td></tr>
        <tr><td class="k">UPSERT (MySQL)</td><td>INSERT INTO t(...) VALUES(...) ON DUPLICATE KEY UPDATE col = VALUES(col)</td></tr>
        <tr><td class="k">SKIP LOCKED</td><td>SELECT ... FOR UPDATE SKIP LOCKED &#x2014; queue pattern, no blocking</td></tr>
        <tr><td class="k">EXPLAIN ANALYZE</td><td>Prefix any query; shows actual rows, time, index use (PostgreSQL)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Transaction Template (Java)</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Code</th></tr>
        <tr><td class="k">Optimistic lock retry</td><td>catch ObjectOptimisticLockingFailureException &#x2192; retry N times with fresh read</td></tr>
        <tr><td class="k">Pessimistic lock</td><td>repo.findByIdWithLock(id) using @Lock(PESSIMISTIC_WRITE)</td></tr>
        <tr><td class="k">Programmatic tx</td><td>TransactionTemplate.execute(status &#x2192; { ... }) &#x2014; finer control than @Transactional</td></tr>
        <tr><td class="k">Read replica routing</td><td>AbstractRoutingDataSource &#x2192; override determineCurrentLookupKey()</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Docker — Production Patterns</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Essential Build Commands</h4>
      <table class="cs-table">
        <tr><th>Command</th><th>Purpose</th></tr>
        <tr><td class="k">docker build -t app:1.0 --no-cache .</td><td>Build image, force fresh layers</td></tr>
        <tr><td class="k">docker buildx build --platform linux/amd64,linux/arm64</td><td>Multi-arch build (M1 Mac &#x2192; AMD64 K8s)</td></tr>
        <tr><td class="k">docker image inspect app:1.0</td><td>View layers, env vars, entrypoint</td></tr>
        <tr><td class="k">docker scout cves app:1.0</td><td>CVE scan without pushing</td></tr>
        <tr><td class="k">docker run --rm -it --entrypoint sh app:1.0</td><td>Debug image interactively</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Dockerfile Best Practices</h4>
      <table class="cs-table">
        <tr><th>Rule</th><th>Why</th></tr>
        <tr><td class="k">Multi-stage build</td><td>Build tools not in runtime image; smaller, less attack surface</td></tr>
        <tr><td class="k">Use JRE not JDK at runtime</td><td>JDK is ~300MB; JRE ~150MB; no compiler in production</td></tr>
        <tr><td class="k">Non-root USER</td><td>Required for OpenShift; security best practice</td></tr>
        <tr><td class="k">COPY deps before src</td><td>Layer cache: deps rebuild only when pom.xml changes</td></tr>
        <tr><td class="k">Use jarmode=layertools</td><td>Spring Boot layer extraction &#x2192; optimal Docker cache</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Docker Compose (dev)</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Snippet</th></tr>
        <tr><td class="k">Health check</td><td>healthcheck: test: [CMD, curl, -f, http://localhost:8080/actuator/health]</td></tr>
        <tr><td class="k">Depends on healthy</td><td>depends_on: db: condition: service_healthy</td></tr>
        <tr><td class="k">Named volume</td><td>volumes: pgdata:/var/lib/postgresql/data</td></tr>
        <tr><td class="k">Override file</td><td>docker-compose.override.yml for local dev; auto-merged</td></tr>
        <tr><td class="k">Profiles</td><td>profiles: [tools] &#x2014; only start with --profile tools flag</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">OpenShift vs Kubernetes — Key Differences</div>
  <div class="cs-grid">
    <div class="cs-card" style="grid-column: 1 / -1;"><h4>Feature Comparison</h4>
      <table class="cs-table">
        <tr><th>Feature</th><th>Vanilla Kubernetes</th><th>OpenShift (OCP)</th></tr>
        <tr><td class="k">Pod Security</td><td>PodSecurityAdmission (PSA) &#x2014; namespaced labels</td><td>Security Context Constraints (SCCs) &#x2014; more granular, cluster-scoped</td></tr>
        <tr><td class="k">Default run-as-root</td><td>Allowed unless PSA enforces restricted</td><td>Blocked by default SCC &#x2018;restricted&#x2019;. Must use numeric non-root UID</td></tr>
        <tr><td class="k">Routes / Ingress</td><td>Ingress (requires controller)</td><td>OpenShift Route (built-in HAProxy; TLS termination native)</td></tr>
        <tr><td class="k">Image Registry</td><td>External (ECR, DockerHub, Artifactory)</td><td>Built-in internal registry</td></tr>
        <tr><td class="k">CI/CD</td><td>Tekton (optional install)</td><td>OpenShift Pipelines (Tekton) built-in; OpenShift GitOps (ArgoCD) built-in</td></tr>
        <tr><td class="k">CLI</td><td>kubectl</td><td>oc (superset of kubectl; adds login, project, new-app, expose)</td></tr>
        <tr><td class="k">Projects</td><td>Namespaces</td><td>Projects = Namespaces + RBAC defaults</td></tr>
        <tr><td class="k">Monitoring</td><td>Install Prometheus stack separately</td><td>Built-in cluster monitoring (Prometheus + Alertmanager + Grafana)</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Spring Boot on OpenShift — Gotchas</h4>
      <table class="cs-table">
        <tr><th>Issue</th><th>Fix</th></tr>
        <tr><td class="k">Container runs as root</td><td>Add USER 1001 in Dockerfile; use numeric UID not username</td></tr>
        <tr><td class="k">Port 8080 not bindable</td><td>Ports &lt;1024 need privilege; 8080 fine; never use 80/443 directly</td></tr>
        <tr><td class="k">Read-only /tmp</td><td>Mount emptyDir at /tmp if app writes temp files</td></tr>
        <tr><td class="k">SCC \'restricted\' blocks volume type</td><td>Use emptyDir, configMap, secret, PVC &#x2014; not hostPath</td></tr>
        <tr><td class="k">oc login token expires</td><td>Use ServiceAccount token in CI, not personal token</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">IBM Stack Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>WebSphere Liberty / Open Liberty</h4>
      <table class="cs-table">
        <tr><th>Concept</th><th>Notes</th></tr>
        <tr><td class="k">server.xml features</td><td>jaxrs-3.0, jdbc-4.3, mpHealth-4.0, mpMetrics-5.0, openidConnectClient-1.0</td></tr>
        <tr><td class="k">Variable substitution</td><td>${env.DB_URL} in server.xml reads from env vars or server.env file</td></tr>
        <tr><td class="k">Liberty Maven Plugin</td><td>liberty:dev for hot reload; liberty:package for uber-jar or Docker layer</td></tr>
        <tr><td class="k">OpenJ9 GC policy</td><td>gencon (default, like G1), balanced, optthruput (like Parallel), metronome (soft RT)</td></tr>
        <tr><td class="k">vs Tomcat</td><td>Liberty supports full Jakarta EE; Tomcat is Servlet/JSP only</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>IBM MQ (JMS)</h4>
      <table class="cs-table">
        <tr><th>Concept</th><th>Notes</th></tr>
        <tr><td class="k">Queue vs Topic</td><td>Queue: point-to-point; Topic: pub-sub with durable subscriptions</td></tr>
        <tr><td class="k">QM (Queue Manager)</td><td>MQ server instance; manages queues, channels, security</td></tr>
        <tr><td class="k">Channel</td><td>Communication path between QMs or app and QM (SVRCONN for apps)</td></tr>
        <tr><td class="k">Spring JMS</td><td>@JmsListener + JmsTemplate; IBM MQ Spring Boot Starter auto-configures</td></tr>
        <tr><td class="k">Exactly-once</td><td>MQ + XA transactions across MQ + DB in same 2PC transaction</td></tr>
        <tr><td class="k">Dead Letter Queue</td><td>SYSTEM.DEAD.LETTER.QUEUE &#x2014; messages that can&#x2019;t be delivered</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>IBM Db2 Quick Reference</h4>
      <table class="cs-table">
        <tr><th>Concept</th><th>Notes</th></tr>
        <tr><td class="k">Schemas</td><td>Default schema = username. SET SCHEMA or fully qualify: schema.table</td></tr>
        <tr><td class="k">Isolation levels</td><td>CS (cursor stability &#x2248; RC), RS (read stability &#x2248; RR), RR, UR (uncommitted read)</td></tr>
        <tr><td class="k">FETCH FIRST N ROWS ONLY</td><td>Db2 equivalent of LIMIT N</td></tr>
        <tr><td class="k">IDENTITY column</td><td>GENERATED ALWAYS AS IDENTITY &#x2014; Db2 autoincrement</td></tr>
        <tr><td class="k">REORGCHK / RUNSTATS</td><td>Db2 equivalent of ANALYZE &#x2014; update statistics, check for REORG need</td></tr>
        <tr><td class="k">Spring Boot driver</td><td>com.ibm.db2.jcc.DB2Driver; jdbc:db2://host:50000/dbname</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Design Patterns — GoF Quick Reference</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Creational</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Use when</th><th>Spring example</th></tr>
        <tr><td class="k">Singleton</td><td>One instance per context</td><td>@Component (default scope)</td></tr>
        <tr><td class="k">Factory Method</td><td>Subclass decides which object to create</td><td>BeanFactory</td></tr>
        <tr><td class="k">Abstract Factory</td><td>Family of related objects without concrete classes</td><td>DataSourceFactory</td></tr>
        <tr><td class="k">Builder</td><td>Complex object construction step by step</td><td>WebClient.builder(), ResponseEntity.ok()</td></tr>
        <tr><td class="k">Prototype</td><td>Clone an existing object</td><td>@Scope("prototype")</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Structural</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Use when</th><th>Spring example</th></tr>
        <tr><td class="k">Adapter</td><td>Incompatible interfaces must work together</td><td>ACL adapters, HandlerAdapter</td></tr>
        <tr><td class="k">Decorator</td><td>Add behaviour without subclassing</td><td>BeanPostProcessor, HttpSecurity</td></tr>
        <tr><td class="k">Fa&#xe7;ade</td><td>Simple interface over complex subsystem</td><td>JdbcTemplate over JDBC API</td></tr>
        <tr><td class="k">Proxy</td><td>Control access; add cross-cutting concerns</td><td>Spring AOP (@Transactional, @Cacheable)</td></tr>
        <tr><td class="k">Composite</td><td>Tree structures treated uniformly</td><td>SecurityFilterChain</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>Behavioural</h4>
      <table class="cs-table">
        <tr><th>Pattern</th><th>Use when</th><th>Spring example</th></tr>
        <tr><td class="k">Strategy</td><td>Interchangeable algorithms</td><td>PaymentStrategy, Comparator</td></tr>
        <tr><td class="k">Observer</td><td>Notify dependents on state change</td><td>@EventListener, ApplicationEventPublisher</td></tr>
        <tr><td class="k">Template Method</td><td>Define skeleton; subclasses fill steps</td><td>JdbcTemplate, AbstractController</td></tr>
        <tr><td class="k">Chain of Responsibility</td><td>Pass request through handlers</td><td>Servlet FilterChain, SecurityFilterChain</td></tr>
        <tr><td class="k">Command</td><td>Encapsulate request as object (undo, queue)</td><td>Saga steps, CompletableFuture tasks</td></tr>
        <tr><td class="k">State</td><td>Behaviour changes based on internal state</td><td>Order state machine, Circuit Breaker states</td></tr>
      </table>
    </div>
  </div>
</div>

<div class="cs-section">
  <div class="cs-section-h">Security — Quick Reference Checklist</div>
  <div class="cs-grid">
    <div class="cs-card"><h4>Spring Security — OAuth2 Resource Server</h4>
      <table class="cs-table">
        <tr><th>Config</th><th>Snippet / Notes</th></tr>
        <tr><td class="k">JWT validation</td><td>spring.security.oauth2.resourceserver.jwt.jwk-set-uri=https://idp/.well-known/jwks.json</td></tr>
        <tr><td class="k">Issuer validation</td><td>spring.security.oauth2.resourceserver.jwt.issuer-uri=https://idp/realm</td></tr>
        <tr><td class="k">Method security</td><td>@EnableMethodSecurity on @Configuration class</td></tr>
        <tr><td class="k">CORS config</td><td>http.cors(c -&gt; c.configurationSource(corsSource))</td></tr>
        <tr><td class="k">CSRF for APIs</td><td>http.csrf(AbstractHttpConfigurer::disable) for stateless JWT APIs</td></tr>
        <tr><td class="k">Security headers</td><td>Automatic in Spring Security; tune via http.headers()</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>API Security Checklist</h4>
      <table class="cs-table">
        <tr><th>Check</th><th>Status</th></tr>
        <tr><td class="k">Validate JWT iss + aud + exp</td><td>Not just signature</td></tr>
        <tr><td class="k">Object-level auth on every endpoint</td><td>BOLA &#x2014; don&#x2019;t skip this</td></tr>
        <tr><td class="k">Rate limiting per user/IP</td><td>Bucket4j or API gateway</td></tr>
        <tr><td class="k">No secrets in code / git</td><td>git-secrets pre-commit hook</td></tr>
        <tr><td class="k">TLS everywhere</td><td>Including internal services</td></tr>
        <tr><td class="k">Dependency CVE scan</td><td>Dependabot / OWASP dependency-check</td></tr>
        <tr><td class="k">Structured error responses</td><td>No stack traces to clients</td></tr>
        <tr><td class="k">Input validation at boundary</td><td>Bean Validation (@Valid) + sanitise</td></tr>
        <tr><td class="k">Actuator endpoints secured</td><td>Expose only health, info externally</td></tr>
      </table>
    </div>
    <div class="cs-card"><h4>GDPR Compliance Checklist</h4>
      <table class="cs-table">
        <tr><th>Requirement</th><th>Implementation approach</th></tr>
        <tr><td class="k">Right to erasure</td><td>Cryptographic erasure (encrypt PII, delete key) or tombstone pattern</td></tr>
        <tr><td class="k">Data minimisation</td><td>Collect only what&#x2019;s needed; document purpose</td></tr>
        <tr><td class="k">Retention limits</td><td>TTL on PII fields; archival with anonymisation</td></tr>
        <tr><td class="k">Audit trail</td><td>Log all PII access (who read what, when)</td></tr>
        <tr><td class="k">Data residency</td><td>EU data stays in EU regions; document in architecture</td></tr>
        <tr><td class="k">Consent tracking</td><td>Immutable consent log with timestamp, version</td></tr>
        <tr><td class="k">Breach notification</td><td>72h to DPA; playbook prepared</td></tr>
      </table>
    </div>
  </div>
</div>
</div>'''

old_cs = '    <div id="cheatsheetContent"></div>'
if old_cs in content:
    content = content.replace(old_cs, '    ' + cheatsheet_static, 1)
    print("✓ Replaced cheatsheetContent with static HTML")
else:
    print("✗ Could not find cheatsheetContent div")

# ══════════════════════════════════════════════════════════════════════
# STEP 3 — Remove the renderCheatSheet IIFE from JS
# ══════════════════════════════════════════════════════════════════════
import re

# Remove everything from the CHEAT SHEET comment to the closing })();
cs_pattern = r'\n// ={60,}\n// CHEAT SHEET\n// ={60,}\n\(function renderCheatSheet\(\).*?\}\)\(\);\n'
cs_match = re.search(cs_pattern, content, re.DOTALL)
if cs_match:
    content = content[:cs_match.start()] + '\n' + content[cs_match.end():]
    print("✓ Removed renderCheatSheet IIFE")
else:
    print("✗ Could not find renderCheatSheet IIFE pattern")

# ══════════════════════════════════════════════════════════════════════
# STEP 4 — Replace renderDiagrams with Miro-style visual content
# ══════════════════════════════════════════════════════════════════════
miro_diagrams = r"""// ============================================================
// DIAGRAMS / ΣΧΗΜΑΤΑ — MIRO-STYLE
// ============================================================
(function renderDiagrams(){
try {
const el=document.getElementById('diagramsContent');
if(!el) return;
el.innerHTML=`

<!-- ─── 1. JVM MEMORY ─────────────────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">JVM — Memory Architecture &amp; GC</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>JVM Memory Regions — Complete Map</h4>
      <div class="mzone org" style="margin-bottom:12px">
        <span class="mzone-lbl">HEAP (-Xmx)</span>
        <div class="m2col" style="gap:12px;margin-top:6px">
          <div class="mzone blu">
            <span class="mzone-lbl">YOUNG GENERATION</span>
            <div class="mrow center" style="margin-top:6px">
              <div class="mbox org wide" style="min-width:130px">EDEN<small>new Obj() / TLAB<br>bump-pointer alloc</small></div>
              <div class="marr">→</div>
              <div class="mbox blu">S0<small>Surv<br>age+1</small></div>
              <div class="marr">⇄</div>
              <div class="mbox blu">S1<small>Surv<br>age+1</small></div>
            </div>
            <div class="mnote info" style="margin-top:8px">Minor GC (STW, &lt;10ms) — runs every time Eden fills</div>
          </div>
          <div class="mzone grn">
            <span class="mzone-lbl">OLD / TENURED</span>
            <div class="mcol" style="gap:8px;margin-top:6px">
              <div class="mbox grn full">long-lived objects<small>promoted after age ≥ 15</small></div>
              <div class="mnote warn">Fills → Full GC (STW, hundreds of ms — avoid!)</div>
            </div>
          </div>
        </div>
      </div>
      <div class="m3col" style="gap:10px">
        <div class="mzone yel"><span class="mzone-lbl">METASPACE (off-heap)</span>
          <div class="mbox yel full" style="margin-top:6px">class metadata<small>bytecode, constant pool<br>-XX:MaxMetaspaceSize=256m</small></div>
        </div>
        <div class="mzone dim"><span class="mzone-lbl">THREAD STACKS (per-thread)</span>
          <div class="mbox dim full" style="margin-top:6px">LIFO frames<small>locals, -Xss 512KB<br>StackOverflowError if deep</small></div>
        </div>
        <div class="mzone grn"><span class="mzone-lbl">CODE CACHE (JIT)</span>
          <div class="mbox grn full" style="margin-top:6px">JIT-compiled native<small>~240MB default<br>warm-up latency</small></div>
        </div>
      </div>
      <div class="key-insight">⚡ Eden = cheap bump-pointer (no lock). Full GC = avoid. Metaspace leak → classloader leak (CGLib, Hibernate proxies). Always -XX:+HeapDumpOnOutOfMemoryError.</div>
    </div>

    <div class="diag-card green">
      <h4>Object Lifetime — GC Flow</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox org full">new Obj() in thread<small>allocated in Eden TLAB</small></div>
        <div class="mvline"></div>
        <div class="mnote warn">Eden fills → Minor GC (STW, fast)</div>
        <div class="mvline"></div>
        <div class="mrow center">
          <div class="mbox blu wide">Survivor S0/S1<small>age++ each GC</small></div>
          <div class="marr">age≥15→</div>
          <div class="mbox red wide">Old Gen<small>Full GC risk</small></div>
        </div>
        <div class="mvline"></div>
        <div class="mnote warn">Unreachable at any stage</div>
        <div class="mvline"></div>
        <div class="mbox grn full fill">reclaimed ✓</div>
      </div>
      <div class="key-insight">⚡ Survivors growing continuously = memory leak. Use JFR + Eclipse MAT to find the retention path.</div>
    </div>

    <div class="diag-card blue">
      <h4>GC Algorithm Ladder</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mrow">
          <div class="mbox red sm wide">Serial GC</div>
          <div class="mnote fail" style="flex:1">Full STW · single-thread · &lt;100MB heap only</div>
        </div>
        <div class="mrow">
          <div class="mbox yel sm wide">Parallel GC</div>
          <div class="mnote warn" style="flex:1">Full STW multi-thread · max throughput · batch/analytics</div>
        </div>
        <div class="mrow">
          <div class="mbox blu sm wide">G1 GC</div>
          <div class="mnote info" style="flex:1">Bounded STW · region-based · safe default Java 9+</div>
        </div>
        <div class="mrow">
          <div class="mbox grn sm wide">ZGC / Shen.</div>
          <div class="mnote ok" style="flex:1">Concurrent · &lt;1ms pause · latency-critical &gt;16GB</div>
        </div>
      </div>
      <div class="key-insight">⚡ Fintech / low-latency: ZGC. General enterprise: G1 with -XX:MaxGCPauseMillis=200.</div>
    </div>

  </div>
</div>

<!-- ─── 2. SPRING BOOT REQUEST LIFECYCLE ───────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Spring Boot — Request Lifecycle &amp; Layers</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>HTTP Request → DB — Complete Flow</h4>
      <div class="mrow center" style="gap:6px;flex-wrap:wrap">
        <div class="mcol">
          <div class="mbox org">Client<small>HTTP</small></div>
        </div>
        <div class="marr">→</div>
        <div class="mzone dim" style="padding:10px 12px">
          <span class="mzone-lbl">Security Layer</span>
          <div class="mrow center" style="margin-top:4px">
            <div class="mbox dim sm">Filter 1<small>CORS</small></div>
            <div class="marr">→</div>
            <div class="mbox dim sm">Filter 2<small>JWT</small></div>
            <div class="marr">→</div>
            <div class="mbox dim sm">Filter N</div>
          </div>
        </div>
        <div class="marr">→</div>
        <div class="mbox blu">DispatcherServlet</div>
        <div class="marr">→</div>
        <div class="mbox yel">HandlerMapping<small>→ find controller</small></div>
        <div class="marr">→</div>
        <div class="mbox org">@RestController<small>@Valid, @PreAuthorize</small></div>
        <div class="marr">→</div>
        <div class="mbox grn">@Service<small>@Transactional</small></div>
        <div class="marr">→</div>
        <div class="mbox blu">@Repository<small>JPA / JDBC</small></div>
        <div class="marr">→</div>
        <div class="mbox dim">DB<small>HikariCP pool</small></div>
      </div>
      <div class="mrow center" style="margin-top:10px;gap:8px">
        <div class="mbadge info">AOP interceptors wrap @Transactional, @Cacheable, @Retry</div>
        <div class="mbadge warn">@ControllerAdvice catches exceptions → ProblemDetail response</div>
      </div>
      <div class="key-insight">⚡ Spring Security filters run before DispatcherServlet. @Transactional is AOP proxy — self-invocation bypasses it. readOnly=true disables dirty checking → faster reads.</div>
    </div>

    <div class="diag-card">
      <h4>Bean Scopes</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mrow">
          <div class="mbox org sm">singleton</div>
          <div class="mnote" style="flex:1">Default · one per ApplicationContext</div>
        </div>
        <div class="mrow">
          <div class="mbox blu sm">prototype</div>
          <div class="mnote" style="flex:1">New instance on every getBean()</div>
        </div>
        <div class="mrow">
          <div class="mbox grn sm">request</div>
          <div class="mnote" style="flex:1">One per HTTP request (web-aware)</div>
        </div>
        <div class="mrow">
          <div class="mbox yel sm">session</div>
          <div class="mnote" style="flex:1">One per HTTP session</div>
        </div>
      </div>
    </div>

    <div class="diag-card blue">
      <h4>Auto-Configuration Order</h4>
      <div class="mcol" style="gap:5px;align-items:stretch">
        <div class="mbox org full">1. @SpringBootApplication<small>triggers @EnableAutoConfiguration</small></div>
        <div class="mvline"></div>
        <div class="mbox blu full">2. spring.factories / AutoConfiguration.imports<small>loads candidate @Configuration classes</small></div>
        <div class="mvline"></div>
        <div class="mbox yel full">3. @Conditional* evaluation<small>@ConditionalOnClass, @ConditionalOnMissingBean</small></div>
        <div class="mvline"></div>
        <div class="mbox grn full">4. Beans registered<small>app beans override auto-configured ones</small></div>
      </div>
    </div>

  </div>
</div>

<!-- ─── 3. KAFKA FLOW ──────────────────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Kafka — Architecture &amp; Delivery Guarantees</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>Kafka Cluster — Internal Structure</h4>
      <div class="m2col" style="gap:16px">
        <div>
          <div class="mrow center" style="margin-bottom:8px">
            <div class="mbox org wide">Producer<small>acks=all<br>idempotent=true</small></div>
            <div class="marr">publish →</div>
            <div class="mzone blu" style="flex:1;padding:10px">
              <span class="mzone-lbl">TOPIC: orders (6 partitions)</span>
              <div class="mrow center" style="margin-top:6px;gap:4px">
                <div class="mbox blu sm">P0<small>Leader</small></div>
                <div class="mbox dim sm">P1<small>Replica</small></div>
                <div class="mbox dim sm">P2<small>Replica</small></div>
                <div class="mbox blu sm">P3<small>Leader</small></div>
                <div class="mbox dim sm">P4<small>Replica</small></div>
                <div class="mbox dim sm">P5<small>Replica</small></div>
              </div>
            </div>
          </div>
          <div class="mrow center">
            <div class="marr" style="transform:rotate(90deg);font-size:22px">↓</div>
          </div>
          <div class="mzone grn" style="margin-top:4px">
            <span class="mzone-lbl">CONSUMER GROUP: order-processor</span>
            <div class="mrow center" style="margin-top:6px;gap:6px">
              <div class="mbox grn sm">Consumer-1<small>P0, P1</small></div>
              <div class="mbox grn sm">Consumer-2<small>P2, P3</small></div>
              <div class="mbox grn sm">Consumer-3<small>P4, P5</small></div>
            </div>
          </div>
        </div>
        <div class="mcol" style="gap:8px;align-items:stretch">
          <span class="msect-h org">Delivery Guarantees</span>
          <div class="mrow">
            <div class="mbox red sm">acks=0</div>
            <div class="mnote fail" style="flex:1">At-most-once · fire &amp; forget</div>
          </div>
          <div class="mrow">
            <div class="mbox yel sm">acks=1</div>
            <div class="mnote warn" style="flex:1">At-most-once · leader crash = loss</div>
          </div>
          <div class="mrow">
            <div class="mbox grn sm">acks=all</div>
            <div class="mnote ok" style="flex:1">At-least-once · waits for ISR</div>
          </div>
          <div class="mrow">
            <div class="mbox grn sm fill">acks=all +<br>idempotent</div>
            <div class="mnote ok" style="flex:1">Exactly-once produce · default Kafka 3</div>
          </div>
          <div class="mrow">
            <div class="mbox org sm">Txn API</div>
            <div class="mnote info" style="flex:1">Exactly-once E2E · fintech use case</div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ Scale consumers = scale partitions (you can't have more consumers than partitions in a group). Lag = (latest offset − committed offset); alert if lag grows unbounded. Compacted topics = event store / cache rebuild.</div>
    </div>

    <div class="diag-card green">
      <h4>Transactional Outbox Pattern</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mzone org"><span class="mzone-lbl">DB Transaction (atomic)</span>
          <div class="mrow center" style="margin-top:6px;gap:6px">
            <div class="mbox org sm">UPDATE orders</div>
            <div class="marr">+</div>
            <div class="mbox org sm">INSERT outbox</div>
          </div>
        </div>
        <div class="mvline"></div>
        <div class="mbox dim full">CDC / Debezium reads outbox table<small>polls or WAL-based change capture</small></div>
        <div class="mvline"></div>
        <div class="mbox grn full fill">Publish to Kafka Topic<small>guaranteed — no dual-write problem</small></div>
      </div>
      <div class="key-insight">⚡ Solves the dual-write problem: DB and Kafka updated in one atomic operation via the outbox table acting as a durable buffer.</div>
    </div>

    <div class="diag-card yellow">
      <h4>Consumer Offset Management</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox org full">Receive batch of messages</div>
        <div class="mvline"></div>
        <div class="mbox yel full">Process each message<small>business logic, DB writes</small></div>
        <div class="mvline"></div>
        <div class="mrow center;gap:6px">
          <div class="mbox grn sm fill">ack.acknowledge()<small>commit offset</small></div>
          <div class="marr">|</div>
          <div class="mbox red sm fill">throw exception<small>→ retry / DLT</small></div>
        </div>
        <div class="mnote warn" style="margin-top:6px">enable-auto-commit=false — always commit after processing, not before</div>
      </div>
    </div>

  </div>
</div>

<!-- ─── 4. KUBERNETES / OPENSHIFT ─────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Kubernetes / OpenShift — Architecture</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>K8s Cluster — Control Plane + Worker Nodes</h4>
      <div class="m2col" style="gap:16px">
        <div class="mzone org">
          <span class="mzone-lbl">CONTROL PLANE</span>
          <div class="m2col" style="gap:8px;margin-top:6px">
            <div class="mbox org sm full">API Server<small>auth, validation, state</small></div>
            <div class="mbox yel sm full">etcd<small>cluster state (CP)</small></div>
            <div class="mbox blu sm full">Scheduler<small>pod → node assignment</small></div>
            <div class="mbox grn sm full">Controller Manager<small>reconciliation loops</small></div>
          </div>
          <div class="mnote info" style="margin-top:8px">OpenShift adds: OAuth server, Image Registry, OperatorHub, OpenShift Routes</div>
        </div>
        <div class="mzone blu">
          <span class="mzone-lbl">WORKER NODE</span>
          <div class="mcol" style="gap:8px;margin-top:6px;align-items:stretch">
            <div class="mbox blu sm full">kubelet<small>manages pod lifecycle</small></div>
            <div class="mbox dim sm full">kube-proxy<small>iptables / IPVS routing</small></div>
            <div class="mzone grn" style="padding:8px">
              <span class="mzone-lbl">POD</span>
              <div class="mrow center" style="margin-top:4px;gap:4px">
                <div class="mbox grn sm">Container<small>app</small></div>
                <div class="mbox dim sm">Sidecar<small>proxy</small></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ OpenShift SCC 'restricted' blocks root containers by default. Use numeric UID (e.g. USER 1001). Routes &gt; Ingress in OCP: built-in HAProxy, TLS termination native.</div>
    </div>

    <div class="diag-card blue">
      <h4>Deployment Strategy Comparison</h4>
      <div class="mcol" style="gap:8px;align-items:stretch">
        <span class="msect-h blu">Rolling Update (default)</span>
        <div class="mrow center">
          <div class="mbox grn sm">v1·v1·v1</div>
          <div class="marr">→</div>
          <div class="mbox org sm">v2·v1·v1</div>
          <div class="marr">→</div>
          <div class="mbox blu sm">v2·v2·v1</div>
          <div class="marr">→</div>
          <div class="mbox grn sm fill">v2·v2·v2</div>
        </div>
        <div class="mnote" style="margin:4px 0">maxSurge=1, maxUnavailable=0 → zero downtime, needs backward-compatible DB schema</div>
        <span class="msect-h blu" style="margin-top:8px">Blue-Green</span>
        <div class="mrow center">
          <div class="mbox blu wide">Blue (v1) LIVE</div>
          <div class="marr">switch</div>
          <div class="mbox grn wide">Green (v2) NEW</div>
        </div>
        <div class="mnote" style="margin:4px 0">Instant cutover, easy rollback, 2x resources needed</div>
        <span class="msect-h grn" style="margin-top:8px">Canary</span>
        <div class="mrow center">
          <div class="mbox grn sm">v1 90%</div>
          <div class="marr">→</div>
          <div class="mbox yel sm">v2 10%</div>
          <div class="marr">→</div>
          <div class="mbox grn sm fill">v2 100%</div>
        </div>
        <div class="mnote ok" style="margin:4px 0">Real traffic validation; needs traffic shaping (Istio / NGINX weights)</div>
      </div>
    </div>

    <div class="diag-card">
      <h4>Pod Probes — Decision Tree</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox org full">startupProbe<small>/actuator/health — once at startup<br>failure: kill + restart</small></div>
        <div class="mnote info">Pass → enables liveness &amp; readiness</div>
        <div class="mvline"></div>
        <div class="mrow center" style="gap:8px">
          <div class="mbox grn wide">livenessProbe<small>continuously<br>fail → restart container</small></div>
          <div class="mbox blu wide">readinessProbe<small>continuously<br>fail → remove from Service</small></div>
        </div>
        <div class="mnote warn">Rule: liveness LESS aggressive than readiness. Never put slow dependency check in liveness — kills healthy pods!</div>
      </div>
    </div>

  </div>
</div>

<!-- ─── 5. OAUTH2 / OIDC / SECURITY ───────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">OAuth2 / OIDC — Flows &amp; JWT Structure</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>Authorization Code Flow (PKCE) — Step by Step</h4>
      <div class="mrow center" style="gap:6px;flex-wrap:wrap">
        <div class="mcol">
          <div class="mbox org">User<small>Browser</small></div>
        </div>
        <div class="marr">1. Login click →</div>
        <div class="mcol">
          <div class="mbox blu">Client App<small>(SPA / backend)</small></div>
        </div>
        <div class="marr">2. /authorize + code_challenge →</div>
        <div class="mcol">
          <div class="mbox yel">Auth Server<small>(Keycloak/Azure)</small></div>
        </div>
      </div>
      <div class="mrow center" style="gap:6px;flex-wrap:wrap;margin-top:8px">
        <div class="mbox org sm">User logs in</div>
        <div class="marr">← 3. redirect + auth_code ←</div>
        <div class="mbox yel sm">Auth Server</div>
      </div>
      <div class="mrow center" style="gap:6px;flex-wrap:wrap;margin-top:8px">
        <div class="mbox blu sm">Client App</div>
        <div class="marr">4. /token + code + code_verifier →</div>
        <div class="mbox yel sm">Auth Server</div>
        <div class="marr">← 5. access_token + id_token + refresh_token ←</div>
      </div>
      <div class="mrow center" style="gap:6px;flex-wrap:wrap;margin-top:8px">
        <div class="mbox blu sm">Client App</div>
        <div class="marr">6. Bearer token →</div>
        <div class="mbox grn sm">Resource Server<small>(Spring Boot API)</small></div>
        <div class="marr">validates JWT →</div>
        <div class="mbox grn sm">Response ✓</div>
      </div>
      <div class="key-insight">⚡ PKCE eliminates auth code interception risk. code_verifier never leaves client. Resource server validates: signature (JWK), iss, aud, exp — all three, every time.</div>
    </div>

    <div class="diag-card blue">
      <h4>JWT Structure</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox org full">HEADER<small>{"alg":"RS256","typ":"JWT"}</small></div>
        <div class="mvline"></div>
        <div class="mbox blu full">PAYLOAD (Claims)<small>iss, sub, aud, exp, iat<br>roles, scope, custom claims</small></div>
        <div class="mvline"></div>
        <div class="mbox grn full">SIGNATURE<small>RS256(base64(header)+'.'+base64(payload), privateKey)</small></div>
        <div class="mnote info" style="margin-top:8px">Validate: signature ✓ | iss matches IdP ✓ | aud matches this service ✓ | exp not expired ✓</div>
        <div class="mnote warn">JWTs are NOT encrypted by default — never put sensitive PII in payload without JWE</div>
      </div>
    </div>

    <div class="diag-card">
      <h4>Circuit Breaker — State Machine</h4>
      <div class="mcol" style="gap:8px;align-items:stretch">
        <div class="mbox grn full fill">CLOSED<small>normal operation<br>counting failures in sliding window</small></div>
        <div class="mvline"></div>
        <div class="mnote fail">failure rate &gt; threshold (e.g. 50%) → OPEN</div>
        <div class="mvline"></div>
        <div class="mbox red full fill">OPEN<small>fast-fail all calls<br>waitDurationInOpenState (60s)</small></div>
        <div class="mvline"></div>
        <div class="mnote warn">timer expires → HALF-OPEN (probe)</div>
        <div class="mvline"></div>
        <div class="mbox yel full">HALF-OPEN<small>permit N test calls<br>permittedCallsInHalfOpenState</small></div>
        <div class="mrow center" style="gap:8px;margin-top:4px">
          <div class="mnote ok" style="flex:1">all pass → CLOSED</div>
          <div class="mnote fail" style="flex:1">any fail → OPEN again</div>
        </div>
      </div>
      <div class="key-insight">⚡ Resilience4j order: @RateLimiter → @CircuitBreaker → @Bulkhead → @Retry → @TimeLimiter (outermost to innermost).</div>
    </div>

  </div>
</div>

<!-- ─── 6. MICROSERVICES PATTERNS ─────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Microservices — Key Patterns</div>
  <div class="diag-grid">

    <div class="diag-card" style="grid-column:1/-1">
      <h4>Saga Pattern — Orchestration vs Choreography</h4>
      <div class="m2col" style="gap:20px">
        <div>
          <span class="msect-h org">Orchestration (central coordinator)</span>
          <div class="mcol" style="gap:6px;align-items:stretch">
            <div class="mbox org full fill">Saga Orchestrator<small>order-service</small></div>
            <div class="mrow center" style="gap:6px">
              <div class="marr" style="transform:rotate(90deg)">↓</div>
              <div class="mbox blu sm">Payment Svc</div>
              <div class="mbox grn sm">Inventory Svc</div>
              <div class="mbox yel sm">Shipping Svc</div>
            </div>
            <div class="mnote ok">Easier audit trail, clear failure point</div>
            <div class="mnote warn">Single point of coupling — orchestrator knows all services</div>
          </div>
        </div>
        <div>
          <span class="msect-h blu">Choreography (event-driven)</span>
          <div class="mrow center" style="gap:6px;flex-wrap:wrap">
            <div class="mbox org sm">Order Svc<small>publishes OrderCreated</small></div>
            <div class="marr">→</div>
            <div class="mbox blu sm">Payment Svc<small>PaymentProcessed</small></div>
            <div class="marr">→</div>
            <div class="mbox grn sm">Inventory Svc<small>StockReserved</small></div>
            <div class="marr">→</div>
            <div class="mbox yel sm">Shipping Svc</div>
          </div>
          <div class="mnote ok" style="margin-top:8px">Decoupled — services don't know each other</div>
          <div class="mnote fail">Hard to trace, compensating tx scattered, cyclic events risk</div>
        </div>
      </div>
      <div class="key-insight">⚡ Use Orchestration when you need clear audit trail and central failure handling (fintech). Use Choreography when services should be truly independent and you have good observability.</div>
    </div>

    <div class="diag-card green">
      <h4>CQRS + Event Sourcing</h4>
      <div class="m2col" style="gap:10px">
        <div class="mzone org">
          <span class="mzone-lbl">COMMAND SIDE (Write)</span>
          <div class="mcol" style="gap:5px;margin-top:6px;align-items:stretch">
            <div class="mbox org sm full">Command Handler</div>
            <div class="mvline"></div>
            <div class="mbox yel sm full">Event Store<small>append-only log</small></div>
            <div class="mvline"></div>
            <div class="mbox dim sm full">Publish domain events</div>
          </div>
        </div>
        <div class="mzone blu">
          <span class="mzone-lbl">QUERY SIDE (Read)</span>
          <div class="mcol" style="gap:5px;margin-top:6px;align-items:stretch">
            <div class="mbox blu sm full">Event Handler<small>builds read models</small></div>
            <div class="mvline"></div>
            <div class="mbox grn sm full">Read DB<small>optimised projections</small></div>
            <div class="mvline"></div>
            <div class="mbox dim sm full">Query API</div>
          </div>
        </div>
      </div>
      <div class="mnote warn" style="margin-top:8px">Eventual consistency — read model lags behind event store</div>
      <div class="key-insight">⚡ Event sourcing = complete audit trail (replay events to any point in time). CQRS = optimise read/write independently. Don't use for simple CRUD.</div>
    </div>

    <div class="diag-card red">
      <h4>Strangler Fig — Legacy Migration</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox dim full">Client Request</div>
        <div class="mvline"></div>
        <div class="mbox yel full">Façade / API Gateway<small>routing layer</small></div>
        <div class="mrow center" style="gap:8px;margin-top:4px">
          <div class="mbox red wide">Legacy Monolith<small>shrinking over time</small></div>
          <div class="marr">|</div>
          <div class="mbox grn wide">New Microservices<small>growing over time</small></div>
        </div>
        <div class="mnote info" style="margin-top:6px">Routes shift from monolith → microservices as features migrate</div>
        <div class="mnote ok">Low risk: old system stays running until fully replaced</div>
      </div>
    </div>

  </div>
</div>

<!-- ─── 7. DATABASE / OBSERVABILITY ───────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Database Patterns &amp; Observability Stack</div>
  <div class="diag-grid">

    <div class="diag-card">
      <h4>Read Replica Routing Pattern</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mrow center">
          <div class="mbox org wide">@Transactional<small>(read-write)</small></div>
          <div class="marr">→</div>
          <div class="mbox red wide fill">PRIMARY<small>writes</small></div>
        </div>
        <div class="mrow center">
          <div class="mbox grn wide">@Transactional<br>(readOnly=true)</div>
          <div class="marr">→</div>
          <div class="mbox blu wide">REPLICA 1/2/3<small>reads — load balanced</small></div>
        </div>
        <div class="mnote info" style="margin-top:8px">AbstractRoutingDataSource.determineCurrentLookupKey() routes based on @Transactional(readOnly)</div>
        <div class="mnote warn">Replica lag means reads may not see latest write — design for eventual consistency or route to primary when freshness needed</div>
      </div>
    </div>

    <div class="diag-card blue">
      <h4>Observability — Three Pillars</h4>
      <div class="m3col" style="gap:8px">
        <div class="mcol" style="gap:5px;align-items:stretch">
          <span class="msect-h org">METRICS</span>
          <div class="mbox org sm full">Micrometer<small>Spring Boot</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox yel sm full">Prometheus<small>scrape /actuator/prometheus</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox org sm full">Grafana<small>dashboards</small></div>
        </div>
        <div class="mcol" style="gap:5px;align-items:stretch">
          <span class="msect-h blu">TRACES</span>
          <div class="mbox blu sm full">Micrometer Tracing<small>auto-instrument</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox blu sm full">Zipkin / Tempo<small>trace store</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox blu sm full">Grafana Tempo<small>trace UI</small></div>
        </div>
        <div class="mcol" style="gap:5px;align-items:stretch">
          <span class="msect-h grn">LOGS</span>
          <div class="mbox grn sm full">Logback / Log4j2<small>structured JSON</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox grn sm full">Loki / ELK<small>log aggregation</small></div>
          <div class="marr" style="margin:0 auto">↓</div>
          <div class="mbox grn sm full">Grafana<small>correlated view</small></div>
        </div>
      </div>
      <div class="mnote info" style="margin-top:10px">traceId + spanId propagated via W3C TraceContext headers — correlate logs ↔ traces ↔ metrics</div>
      <div class="key-insight">⚡ P99 latency in Grafana + correlated trace in Tempo + error log in Loki = root cause in &lt;5 minutes. Always log traceId with every log line.</div>
    </div>

    <div class="diag-card green">
      <h4>HikariCP Pool — Sizing Model</h4>
      <div class="mzone org">
        <span class="mzone-lbl">Formula</span>
        <div class="mbox yel full" style="margin-top:6px;font-size:13px">pool_size = (cores × 2) + effective_spindle_count</div>
      </div>
      <div class="mcol" style="gap:6px;margin-top:10px;align-items:stretch">
        <div class="mnote ok">Example: 4 cores × 2 + 1 SSD = ~10 connections per service instance</div>
        <div class="mnote warn">Too many connections = DB thrash + context switching overhead</div>
        <div class="mnote info">HikariCP metrics via Micrometer: hikaricp.connections.active, .pending, .timeout</div>
        <div class="mrow center" style="margin-top:8px;gap:6px">
          <div class="mbox org sm">connection-timeout: 30s</div>
          <div class="mbox yel sm">idle-timeout: 10min</div>
          <div class="mbox grn sm">max-lifetime: 30min</div>
        </div>
      </div>
    </div>

  </div>
</div>

`;
} catch(e) { console.error('renderDiagrams error:', e); }
})();"""

# Find and replace the renderDiagrams IIFE
diag_pattern = r'// ={60,}\n// DIAGRAMS / ΣΧΗΜΑΤΑ\n// ={60,}\n\(function renderDiagrams\(\)\{.*?\}\)\(\);'
diag_match = re.search(diag_pattern, content, re.DOTALL)
if diag_match:
    content = content[:diag_match.start()] + miro_diagrams + content[diag_match.end():]
    print("✓ Replaced renderDiagrams with Miro-style content")
else:
    print("✗ Could not find renderDiagrams IIFE pattern")
    # Try simpler pattern
    diag_pattern2 = r'// DIAGRAMS / ΣΧΗΜΑΤΑ\n// ={60,}\n\(function renderDiagrams'
    m2 = re.search(diag_pattern2, content, re.DOTALL)
    if m2:
        print(f"  Found partial match at {m2.start()}")
    else:
        print("  No partial match either")

# ══════════════════════════════════════════════════════════════════════
# WRITE OUTPUT
# ══════════════════════════════════════════════════════════════════════
with open('/home/user/IV/senior-architect-prep.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ File written")
print(f"  Total lines: {content.count(chr(10))}")

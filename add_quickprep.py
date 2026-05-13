#!/usr/bin/env python3
"""Add Quick Prep tab + more Miro diagrams."""
import re

with open('/home/user/IV/senior-architect-prep.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════════════════════════
# STEP 1 — Add Quick Prep CSS before </style>
# ══════════════════════════════════════════════════════════════════════
qp_css = """
  /* ===== QUICK PREP TAB ===== */
  .qp-wrap { display: grid; gap: 16px; }
  .qp-block {
    border: 1px solid var(--border); background: var(--bg-card);
    border-radius: 12px; overflow: hidden;
  }
  .qp-header {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 16px; border-bottom: 1px solid var(--border);
    background: var(--bg-elev);
  }
  .qp-timer-badge {
    font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;
    padding: 3px 9px; border-radius: 20px; background: var(--accent);
    color: #000; flex-shrink: 0; letter-spacing: .05em;
  }
  .qp-timer-badge.b { background: var(--info); }
  .qp-timer-badge.g { background: var(--done); }
  .qp-timer-badge.y { background: var(--warn); }
  .qp-timer-badge.r { background: var(--crit); }
  .qp-title {
    font-family: 'Fraunces', serif; font-size: 15px; font-weight: 600;
    color: var(--text); flex: 1;
  }
  .qp-body { padding: 14px 16px; }
  .qp-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }
  .qp-card {
    border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px;
    background: var(--bg-elev);
  }
  .qp-card-h {
    font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;
    text-transform: uppercase; letter-spacing: .1em; color: var(--accent);
    margin-bottom: 8px; padding-bottom: 5px; border-bottom: 1px dashed var(--border);
  }
  .qp-card-h.b { color: var(--info); }
  .qp-card-h.g { color: var(--done); }
  .qp-card-h.y { color: var(--warn); }
  .qp-card-h.r { color: var(--crit); }
  .qp-list { list-style: none; margin: 0; padding: 0; }
  .qp-list li {
    font-size: 12px; line-height: 1.55; padding: 3px 0;
    border-bottom: 1px solid rgba(255,255,255,.04);
    color: var(--text-dim);
  }
  .qp-list li:last-child { border-bottom: none; }
  .qp-list li strong { color: var(--text); font-weight: 600; }
  .qp-list li code {
    font-family: 'JetBrains Mono', monospace; font-size: 10.5px;
    background: var(--bg-deep); padding: 1px 5px; border-radius: 3px;
    color: var(--accent);
  }
  .qp-bullet::before { content: '▸ '; color: var(--accent); font-size: 10px; }
  .qp-bullet.b::before { color: var(--info); }
  .qp-bullet.g::before { color: var(--done); }
  .qp-bullet.y::before { color: var(--warn); }
  .qp-bullet.r::before { color: var(--crit); }
  .qp-flash {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 8px;
    margin-top: 4px;
  }
  .qp-pill {
    font-family: 'JetBrains Mono', monospace; font-size: 10.5px;
    background: var(--bg-deep); border: 1px solid var(--border);
    border-radius: 6px; padding: 5px 10px; line-height: 1.4; color: var(--text-dim);
  }
  .qp-pill strong { color: var(--text); display: block; font-size: 11px; }
  .qp-intro {
    background: var(--accent-soft); border: 1px solid rgba(255,107,53,.3);
    border-radius: 10px; padding: 14px 18px; margin-bottom: 16px;
    font-family: 'JetBrains Mono', monospace; font-size: 11.5px; color: var(--text);
    line-height: 1.6;
  }
  .qp-intro strong { color: var(--accent); }
  .qp-mantra {
    background: var(--bg-elev); border-left: 4px solid var(--accent);
    border-radius: 0 8px 8px 0; padding: 10px 14px; margin: 6px 0;
    font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text);
    line-height: 1.55;
  }
  .qp-mantra.b { border-left-color: var(--info); }
  .qp-mantra.g { border-left-color: var(--done); }
  .qp-mantra.y { border-left-color: var(--warn); }
  .qp-mantra.r { border-left-color: var(--crit); }
  .qp-code {
    font-family: 'JetBrains Mono', monospace; font-size: 10.5px;
    background: #04080d; border: 1px solid #16202e; border-radius: 6px;
    padding: 8px 12px; line-height: 1.65; overflow-x: auto; color: var(--text-dim);
    margin: 6px 0; white-space: pre;
  }
  .qp-code .a { color: var(--accent); }
  .qp-code .b { color: var(--info); }
  .qp-code .g { color: var(--done); }
  .qp-code .y { color: var(--warn); }
  .qp-code .d { color: #4b5563; }
"""

content = content.replace('</style>\n</head>', qp_css + '</style>\n</head>', 1)
print("✓ Added Quick Prep CSS")

# ══════════════════════════════════════════════════════════════════════
# STEP 2 — Add Quick Prep tab button
# ══════════════════════════════════════════════════════════════════════
old_tabs = '''    <button class="tab-btn" data-tab="diagrams">Σχήματα</button>'''
new_tabs = '''    <button class="tab-btn" data-tab="diagrams">Σχήματα</button>
    <button class="tab-btn" data-tab="quickprep">⚡ Quick Prep</button>'''

if old_tabs in content:
    content = content.replace(old_tabs, new_tabs, 1)
    print("✓ Added Quick Prep tab button")
else:
    print("✗ Could not find tab buttons")

# ══════════════════════════════════════════════════════════════════════
# STEP 3 — Add Quick Prep tab pane (STATIC HTML)
# ══════════════════════════════════════════════════════════════════════
quickprep_html = '''
  <div class="tab-pane" id="tab-quickprep">
<div class="qp-intro">
  <strong>⚡ 30-Minute Pre-Interview Blitz</strong><br>
  Read this in order. Each block = ~5 minutes. Don't memorise — <strong>trigger the pattern</strong> so it surfaces naturally under pressure. You know this already.
</div>

<div class="qp-wrap">

<!-- ═══ BLOCK 1: Architecture Mindset (0-5 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge">0 – 5 min</span>
    <span class="qp-title">Architecture Mindset — The Answers That Win</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra">Always trade-off explicitly: <strong>Consistency vs Availability vs Latency vs Cost</strong>. Never say "it depends" alone — say it, then explain which side you'd pick and why.</div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h">Design a system? Use this frame:</div>
        <ul class="qp-list">
          <li class="qp-bullet"><strong>Requirements</strong> — functional, then non-functional (SLA, scale, latency)</li>
          <li class="qp-bullet"><strong>Capacity</strong> — QPS, data size, read/write ratio</li>
          <li class="qp-bullet"><strong>High-level</strong> — boxes and arrows, identify bottlenecks</li>
          <li class="qp-bullet"><strong>Deep-dive</strong> — DB schema, API contracts, failure modes</li>
          <li class="qp-bullet"><strong>Resilience</strong> — Circuit Breaker, Retry, Bulkhead, timeout</li>
          <li class="qp-bullet"><strong>Observability</strong> — metrics + traces + logs = one traceId</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h">Killer one-liners to memorise</div>
        <ul class="qp-list">
          <li class="qp-bullet"><strong>CAP theorem</strong> — "In a partition, pick C or A. We pick CP because bank-grade consistency."</li>
          <li class="qp-bullet"><strong>Saga</strong> — "Orchestration when I need audit trail; choreography when services must be independent."</li>
          <li class="qp-bullet"><strong>Outbox</strong> — "Solves the dual-write problem — DB + event in one atomic tx."</li>
          <li class="qp-bullet"><strong>CQRS</strong> — "Separate read/write models when query patterns diverge from write model."</li>
          <li class="qp-bullet"><strong>Strangler Fig</strong> — "Route by route, monolith shrinks, microservice grows. Zero big-bang."</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h">Patterns → when to use / avoid</div>
        <ul class="qp-list">
          <li class="qp-bullet"><strong>Microservices</strong> — team ≥15, bounded domain. Avoid: still discovering domain.</li>
          <li class="qp-bullet"><strong>Event Sourcing</strong> — audit trail mandatory, temporal queries. Avoid: simple CRUD.</li>
          <li class="qp-bullet"><strong>Canary deploy</strong> — real traffic validation. Avoid: incompatible DB migrations.</li>
          <li class="qp-bullet"><strong>Circuit Breaker</strong> — flaky downstream. Avoid: dependency required for correctness.</li>
          <li class="qp-bullet"><strong>ACL</strong> — you don't control the external model. Avoid: you control both sides.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 2: Java + Spring Boot (5-10 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge b">5 – 10 min</span>
    <span class="qp-title">Java 21 + Spring Boot — Must-Know Answers</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra b">Virtual Threads (Java 21): <strong>1 platform thread per blocking call → thousands of virtual threads. No more thread pool sizing for I/O-bound work. Enable: spring.threads.virtual.enabled=true</strong></div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h b">@Transactional — 5 gotchas</div>
        <ul class="qp-list">
          <li class="qp-bullet b"><strong>Self-invocation</strong> = proxy bypassed → tx ignored. Fix: inject self.</li>
          <li class="qp-bullet b"><strong>private method</strong> = AOP can't proxy. Must be public.</li>
          <li class="qp-bullet b"><strong>readOnly=true</strong> = Hibernate skips dirty check. Use on all reads.</li>
          <li class="qp-bullet b"><strong>REQUIRES_NEW</strong> = suspends outer tx. Use for audit log.</li>
          <li class="qp-bullet b"><strong>rollbackFor</strong> = default is unchecked only. Add <code>Exception.class</code> if needed.</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h b">N+1 Problem — Detection + Fix</div>
        <ul class="qp-list">
          <li class="qp-bullet b"><strong>Symptom</strong> — 1 query for list + N queries for each child</li>
          <li class="qp-bullet b"><strong>Detect</strong> — <code>generate_statistics=true</code>, Hypersistence Optimizer</li>
          <li class="qp-bullet b"><strong>Fix 1</strong> — <code>@Query("JOIN FETCH")</code> in repository</li>
          <li class="qp-bullet b"><strong>Fix 2</strong> — <code>@EntityGraph</code> on method</li>
          <li class="qp-bullet b"><strong>Fix 3</strong> — <code>@BatchSize(25)</code> on collection → IN-clause</li>
          <li class="qp-bullet b"><strong>Fix 4</strong> — <code>default_batch_fetch_size=25</code> globally</li>
          <li class="qp-bullet b"><strong>Never</strong> — EAGER fetch on @ManyToOne (it's the default! change to LAZY)</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h b">GC — Which to pick</div>
        <ul class="qp-list">
          <li class="qp-bullet b"><strong>G1GC</strong> — default Java 9+, 4GB+ heap, general enterprise ✓</li>
          <li class="qp-bullet b"><strong>ZGC</strong> — &lt;1ms pause, latency-critical, &gt;16GB heap</li>
          <li class="qp-bullet b"><strong>Parallel</strong> — max throughput, batch analytics, don't care about pauses</li>
          <li class="qp-bullet b"><strong>Always set</strong> — <code>-XX:MaxRAMPercentage=75</code> in containers</li>
          <li class="qp-bullet b"><strong>Always set</strong> — <code>-XX:+HeapDumpOnOutOfMemoryError</code></li>
          <li class="qp-bullet b"><strong>Metaspace leak</strong> → classloader leak (CGLib, Hibernate proxies, hot reload)</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h b">Spring Security Quick Config</div>
        <div class="qp-code"><span class="b">@Bean</span> SecurityFilterChain sec(<span class="b">HttpSecurity</span> h) {
  <span class="d">// JWT resource server</span>
  h.oauth2ResourceServer(o -> o.jwt(j ->
    j.jwkSetUri(<span class="a">"https://idp/.well-known/jwks"</span>)));
  <span class="d">// stateless → disable CSRF</span>
  h.csrf(c -> c.disable());
  <span class="d">// method security → @PreAuthorize</span>
  <span class="g">@EnableMethodSecurity</span> <span class="d">// on @Configuration</span>
  <span class="d">// validate: iss + aud + exp always</span>
}</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 3: Kafka + Messaging (10-15 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge g">10 – 15 min</span>
    <span class="qp-title">Kafka &amp; Messaging — Core Patterns</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra g"><strong>Scale rule</strong>: consumers in a group ≤ partitions. More consumers than partitions = idle consumers. Scale by adding partitions first, then consumers.</div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h g">Delivery semantics — answer instantly</div>
        <ul class="qp-list">
          <li class="qp-bullet g"><code>acks=0</code> → at-most-once. Fire &amp; forget. OK for metrics.</li>
          <li class="qp-bullet g"><code>acks=1</code> → at-most-once. Leader crash = message lost.</li>
          <li class="qp-bullet g"><code>acks=all</code> → at-least-once. Safe, may duplicate. Consumer must be idempotent.</li>
          <li class="qp-bullet g"><code>acks=all + idempotent=true</code> → exactly-once produce (Kafka 3 default).</li>
          <li class="qp-bullet g"><strong>Transactional API</strong> → exactly-once end-to-end. Use for fintech, never for analytics.</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h g">Kafka vs IBM MQ — when to use which</div>
        <ul class="qp-list">
          <li class="qp-bullet g"><strong>Kafka</strong> — high-throughput, event streaming, event sourcing, log replay, CDC</li>
          <li class="qp-bullet g"><strong>IBM MQ</strong> — enterprise guaranteed delivery, XA 2PC with DB, existing IBM stack</li>
          <li class="qp-bullet g"><strong>MQ strength</strong> — exactly-once across MQ + DB in one XA transaction</li>
          <li class="qp-bullet g"><strong>Kafka strength</strong> — millions of events/sec, consumer groups, log compaction</li>
          <li class="qp-bullet g"><strong>DLQ</strong> — both support dead-letter queues. Configure max retries + DLT topic in Spring Kafka.</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h g">Spring Kafka — production config</div>
        <div class="qp-code">consumer:
  <span class="g">enable-auto-commit: false</span>  <span class="d"># always</span>
  auto-offset-reset: earliest
  isolation-level: read-committed <span class="d"># for txn producers</span>
producer:
  <span class="g">acks: all</span>
  enable-idempotence: true
  retries: 3
listener:
  ack-mode: MANUAL_IMMEDIATE
  concurrency: <span class="a">6</span>  <span class="d"># = partition count</span></div>
      </div>
      <div class="qp-card">
        <div class="qp-card-h g">Outbox Pattern — the answer to "how do you publish reliably?"</div>
        <ul class="qp-list">
          <li class="qp-bullet g">Problem: UPDATE table + publish event = two writes, one may fail</li>
          <li class="qp-bullet g">Solution: <strong>INSERT into outbox table in same DB tx as business data</strong></li>
          <li class="qp-bullet g">CDC (Debezium) reads outbox → publishes to Kafka</li>
          <li class="qp-bullet g">No dual-write, no message loss, guaranteed ordering per aggregate</li>
          <li class="qp-bullet g">Trade-off: CDC infra complexity, slight latency vs. direct publish</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 4: K8s / OpenShift / Docker (15-20 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge y">15 – 20 min</span>
    <span class="qp-title">Docker · Kubernetes · OpenShift — Production Essentials</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra y"><strong>OpenShift rule #1</strong>: Containers run as non-root by default (SCC 'restricted'). Use <code>USER 1001</code> (numeric UID) in Dockerfile. Never <code>USER root</code>.</div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h y">Dockerfile — production checklist</div>
        <div class="qp-code"><span class="d"># Stage 1: build</span>
FROM eclipse-temurin:21-jdk AS build
COPY . .
RUN ./mvnw package -DskipTests

<span class="d"># Stage 2: runtime (JRE only)</span>
FROM eclipse-temurin:<span class="g">21-jre</span>
<span class="g">USER 1001</span>          <span class="d"># OpenShift compat</span>
COPY --from=build target/app.jar app.jar
ENTRYPOINT [<span class="a">"java"</span>, <span class="a">"-jar"</span>, <span class="a">"app.jar"</span>]
EXPOSE 8080       <span class="d"># document only</span></div>
      </div>
      <div class="qp-card">
        <div class="qp-card-h y">Pod probes — never confuse these</div>
        <ul class="qp-list">
          <li class="qp-bullet y"><strong>startupProbe</strong> — fires once. Fail = kill+restart. Give Spring Boot 60s to start.</li>
          <li class="qp-bullet y"><strong>livenessProbe</strong> — fires always. Fail = restart container. <strong>MUST be fast &amp; self-contained</strong> — no DB check!</li>
          <li class="qp-bullet y"><strong>readinessProbe</strong> — fires always. Fail = remove from Service endpoint. OK to check DB/deps here.</li>
          <li class="qp-bullet y">Spring Boot: <code>/actuator/health/liveness</code> and <code>/actuator/health/readiness</code> built-in</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h y">K8s resources — sizing rule</div>
        <ul class="qp-list">
          <li class="qp-bullet y"><strong>Memory request = memory limit</strong> (predictable scheduling, no OOM surprise)</li>
          <li class="qp-bullet y"><strong>CPU request &lt; CPU limit</strong> (allow bursting; throttled if exceeded, not killed)</li>
          <li class="qp-bullet y">Spring Boot: <code>-XX:MaxRAMPercentage=75</code> so JVM fits in container limit</li>
          <li class="qp-bullet y">OOM killed by K8s: raise limit. CPU throttled: raise request first.</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h y">OpenShift — key differences vs K8s</div>
        <ul class="qp-list">
          <li class="qp-bullet y"><strong>Route</strong> (OCP) vs <strong>Ingress</strong> (K8s) — Route has built-in TLS, HAProxy</li>
          <li class="qp-bullet y"><strong>SCC</strong> (OCP) vs <strong>PSA</strong> (K8s) — SCC more granular, cluster-scoped</li>
          <li class="qp-bullet y"><strong>oc</strong> = superset of kubectl. <code>oc new-project</code>, <code>oc expose</code>, <code>oc login</code></li>
          <li class="qp-bullet y"><strong>Built-in</strong>: image registry, Tekton Pipelines, ArgoCD GitOps, Prometheus monitoring</li>
          <li class="qp-bullet y"><strong>S2I</strong> (Source-to-Image) — build inside cluster from source; OCP's BuildConfig</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 5: Security + Resilience (20-25 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge r">20 – 25 min</span>
    <span class="qp-title">Security · Resilience4j · Observability</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra r"><strong>JWT validation mantra</strong>: signature → issuer (iss) → audience (aud) → expiry (exp). All four, every request. Never skip audience check.</div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h r">OAuth2 flow — explain in 30 seconds</div>
        <ul class="qp-list">
          <li class="qp-bullet r">User clicks login → Client redirects to <strong>Auth Server</strong> with <code>code_challenge</code> (PKCE)</li>
          <li class="qp-bullet r">User authenticates → Auth Server redirects with <code>auth_code</code></li>
          <li class="qp-bullet r">Client exchanges code + <code>code_verifier</code> → gets <strong>access_token (JWT) + refresh_token</strong></li>
          <li class="qp-bullet r">Client calls API with <code>Bearer {token}</code> → Resource Server validates JWT locally (JWK public key)</li>
          <li class="qp-bullet r">PKCE prevents code interception — code_verifier never leaves the client</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h r">Resilience4j — annotation order (outermost → innermost)</div>
        <ul class="qp-list">
          <li class="qp-bullet r"><strong>1. @RateLimiter</strong> — reject early, before acquiring any resources</li>
          <li class="qp-bullet r"><strong>2. @CircuitBreaker</strong> — fail fast if service known bad</li>
          <li class="qp-bullet r"><strong>3. @Bulkhead</strong> — limit concurrent calls to downstream</li>
          <li class="qp-bullet r"><strong>4. @Retry</strong> — retry transient failures (with exponential backoff)</li>
          <li class="qp-bullet r"><strong>5. @TimeLimiter</strong> — bound total wall-clock time (innermost)</li>
          <li class="qp-bullet r">Circuit states: <strong>CLOSED → OPEN → HALF-OPEN → CLOSED/OPEN</strong></li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h r">OWASP API Top 10 — architect's view</div>
        <ul class="qp-list">
          <li class="qp-bullet r"><strong>BOLA</strong> (Broken Object Level Auth) — check ownership on every resource endpoint</li>
          <li class="qp-bullet r"><strong>Broken Auth</strong> — validate JWT iss+aud+exp; short-lived tokens; refresh rotation</li>
          <li class="qp-bullet r"><strong>Mass Assignment</strong> — use DTOs, never bind request directly to @Entity</li>
          <li class="qp-bullet r"><strong>Injection</strong> — parameterised queries always; never string concat SQL</li>
          <li class="qp-bullet r"><strong>Security Misconfiguration</strong> — disable Actuator sensitive endpoints; no stack traces to clients</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h r">Observability — 3 pillars summary</div>
        <ul class="qp-list">
          <li class="qp-bullet r"><strong>Metrics</strong> — Micrometer → Prometheus → Grafana. Track P99 latency, error rate, saturation.</li>
          <li class="qp-bullet r"><strong>Traces</strong> — Micrometer Tracing → Zipkin/Tempo. <code>traceId</code> in every log line via MDC.</li>
          <li class="qp-bullet r"><strong>Logs</strong> — structured JSON (ECS format), Loki / ELK. Correlate by traceId.</li>
          <li class="qp-bullet r"><strong>Alert thresholds</strong> — error rate &gt;1%, P99 &gt;500ms, DB pool pending &gt;0, Kafka lag growing.</li>
          <li class="qp-bullet r"><code>management.tracing.sampling.probability=0.1</code> in prod (10% sample rate)</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 6: IBM Stack (25-28 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge" style="background:#8b5cf6;color:#fff">25 – 28 min</span>
    <span class="qp-title">IBM Stack — WebSphere Liberty, MQ, Db2</span>
  </div>
  <div class="qp-body">
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h">WebSphere Liberty key facts</div>
        <ul class="qp-list">
          <li class="qp-bullet"><strong>Features in server.xml</strong> — jaxrs-3.0, jdbc-4.3, mpHealth-4.0, openidConnectClient-1.0</li>
          <li class="qp-bullet"><strong>vs Tomcat</strong> — Liberty = full Jakarta EE; Tomcat = Servlet/JSP only; Liberty lighter than WAS full profile</li>
          <li class="qp-bullet"><strong>Container image</strong> — <code>icr.io/appcafe/open-liberty:kernel-slim-java21-openj9-ubi</code></li>
          <li class="qp-bullet"><strong>Hot reload</strong> — <code>liberty:dev</code> Maven goal; watches src + config</li>
          <li class="qp-bullet"><strong>OpenJ9 GC</strong> — gencon (default ≈ G1), balanced, optthruput (≈ Parallel), metronome (soft realtime)</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h">IBM MQ — the key concepts</div>
        <ul class="qp-list">
          <li class="qp-bullet"><strong>Queue Manager (QM)</strong> — the MQ server; manages queues, channels, security</li>
          <li class="qp-bullet"><strong>Queue</strong> — point-to-point. <strong>Topic</strong> — pub-sub with durable subscriptions.</li>
          <li class="qp-bullet"><strong>Channel (SVRCONN)</strong> — connection path from app to QM</li>
          <li class="qp-bullet"><strong>Exactly-once</strong> — MQ + DB in XA transaction (2PC). Spring JMS + @Transactional(transactionManager="jmsTransactionManager")</li>
          <li class="qp-bullet"><strong>DLQ</strong> — SYSTEM.DEAD.LETTER.QUEUE — failed message parking</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h">Db2 — syntax differences from PG</div>
        <ul class="qp-list">
          <li class="qp-bullet"><code>FETCH FIRST 10 ROWS ONLY</code> — not <code>LIMIT 10</code></li>
          <li class="qp-bullet"><code>GENERATED ALWAYS AS IDENTITY</code> — autoincrement</li>
          <li class="qp-bullet"><code>REORGCHK / RUNSTATS</code> — like PostgreSQL <code>ANALYZE</code></li>
          <li class="qp-bullet">Isolation: <strong>CS</strong> (≈ READ COMMITTED), <strong>RS</strong> (≈ REPEATABLE READ), <strong>RR</strong>, <strong>UR</strong></li>
          <li class="qp-bullet">Spring driver: <code>com.ibm.db2.jcc.DB2Driver</code>, URL: <code>jdbc:db2://host:50000/dbname</code></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ═══ BLOCK 7: Behavioral + Mindset (28-30 min) ═══ -->
<div class="qp-block">
  <div class="qp-header">
    <span class="qp-timer-badge g">28 – 30 min</span>
    <span class="qp-title">Behavioral &amp; Senior Architect Mindset — Last 2 Minutes</span>
  </div>
  <div class="qp-body">
    <div class="qp-mantra g">You are not a developer who writes code. <strong>You are the person who decides what gets built, why, and what the consequences are.</strong> Own that posture in every answer.</div>
    <div class="qp-grid">
      <div class="qp-card">
        <div class="qp-card-h g">STAR answers — have these ready</div>
        <ul class="qp-list">
          <li class="qp-bullet g"><strong>"Disagreed with team"</strong> — data-backed, proposed experiment, deferred to consensus with documented risk.</li>
          <li class="qp-bullet g"><strong>"System went down"</strong> — I led incident, immediate mitigation first, root cause after. Post-mortem with action items.</li>
          <li class="qp-bullet g"><strong>"Legacy modernization"</strong> — Strangler Fig, Anticorruption Layer. Incremental, measurable wins, business buy-in at each step.</li>
          <li class="qp-bullet g"><strong>"Technical debt"</strong> — tracked as first-class backlog items, presented business impact, prioritised with product.</li>
          <li class="qp-bullet g"><strong>"Mentor junior"</strong> — code review + pair programming + design docs. Goal = make them independent, not dependent.</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h g">Questions to ask THEM (signal seniority)</div>
        <ul class="qp-list">
          <li class="qp-bullet g">"What does the current observability stack look like — are you on OpenTelemetry?"</li>
          <li class="qp-bullet g">"How do teams handle cross-service contracts — consumer-driven contract tests, AsyncAPI?"</li>
          <li class="qp-bullet g">"What's the biggest architectural pain point the team is living with right now?"</li>
          <li class="qp-bullet g">"How does release decision authority work — who owns the go/no-go?"</li>
          <li class="qp-bullet g">"What does the onboarding experience look like for a new senior engineer?"</li>
        </ul>
      </div>
      <div class="qp-card">
        <div class="qp-card-h g">Architecture decision framing (ADR style)</div>
        <ul class="qp-list">
          <li class="qp-bullet g"><strong>Context</strong> — what problem, what constraints</li>
          <li class="qp-bullet g"><strong>Options considered</strong> — always 2-3, with trade-offs</li>
          <li class="qp-bullet g"><strong>Decision</strong> — what and why</li>
          <li class="qp-bullet g"><strong>Consequences</strong> — what gets harder, what gets easier</li>
          <li class="qp-bullet g">Say: "The trade-off I accepted is X in exchange for Y" — this shows senior thinking.</li>
        </ul>
      </div>
    </div>
    <div class="qp-mantra" style="margin-top:12px;border-left-color:var(--accent)">
      <strong>Final thought:</strong> They're not testing if you know every API. They're testing if you <strong>think like someone they'd trust with production</strong>. Be deliberate, cite trade-offs, admit what you'd look up. That's the answer.
    </div>
  </div>
</div>

</div><!-- /qp-wrap -->
  </div><!-- /tab-pane#quickprep -->
'''

old_diag_end = '  </div><!-- /tab-pane#diagrams -->'
new_with_quickprep = '  </div><!-- /tab-pane#diagrams -->' + quickprep_html

if old_diag_end in content:
    content = content.replace(old_diag_end, new_with_quickprep, 1)
    print("✓ Added Quick Prep tab pane")
else:
    print("✗ Could not find diagrams pane end")

# ══════════════════════════════════════════════════════════════════════
# STEP 4 — Add more Miro diagrams inside the renderDiagrams template
# ══════════════════════════════════════════════════════════════════════
new_diagram_sections = r"""
<!-- ─── 8. SPRING SECURITY FILTER CHAIN ──────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Spring Security — Filter Chain &amp; OAuth2 Resource Server</div>
  <div class="diag-grid">
    <div class="diag-card" style="grid-column:1/-1">
      <h4>Request → SecurityFilterChain — Every Filter in Order</h4>
      <div class="mrow center" style="gap:5px;flex-wrap:wrap">
        <div class="mbox dim sm">HTTP Request</div>
        <div class="marr">→</div>
        <div class="mbox dim sm">DisableEncoding<br>Filter</div>
        <div class="marr">→</div>
        <div class="mbox red sm">CORS<br>Filter</div>
        <div class="marr">→</div>
        <div class="mbox red sm">CSRF<br>Filter</div>
        <div class="marr">→</div>
        <div class="mbox yel sm">Session<br>Management</div>
        <div class="marr">→</div>
        <div class="mbox org sm">Bearer Token<br>Auth Filter<br><small>JWT decode</small></div>
        <div class="marr">→</div>
        <div class="mbox org sm">Authorization<br>Filter<br><small>RBAC check</small></div>
        <div class="marr">→</div>
        <div class="mbox grn sm">DispatcherServlet<br><small>controller</small></div>
      </div>
      <div class="m2col" style="gap:12px;margin-top:12px">
        <div>
          <span class="msect-h org">JWT Validation Steps (Resource Server)</span>
          <div class="mcol" style="gap:5px;align-items:stretch">
            <div class="mbox dim full">Receive Bearer token from Authorization header</div>
            <div class="mvline"></div>
            <div class="mbox yel full">Fetch JWK Set from jwk-set-uri<small>(cached; refresh on unknown kid)</small></div>
            <div class="mvline"></div>
            <div class="mbox org full">Verify RS256/ES256 signature</div>
            <div class="mvline"></div>
            <div class="mrow center" style="gap:6px">
              <div class="mbox org sm">Check iss<small>= IdP URI</small></div>
              <div class="mbox org sm">Check aud<small>= this service</small></div>
              <div class="mbox org sm">Check exp<small>not expired</small></div>
            </div>
            <div class="mvline"></div>
            <div class="mbox grn full fill">SecurityContext populated — proceed ✓</div>
          </div>
        </div>
        <div>
          <span class="msect-h red">Common Security Mistakes</span>
          <div class="mcol" style="gap:6px;align-items:stretch">
            <div class="mnote fail">Checking signature only — iss/aud bypass → BOLA</div>
            <div class="mnote fail">Logging JWT in plain text — token leaks</div>
            <div class="mnote fail">Not checking object ownership in service layer — mass data leak</div>
            <div class="mnote fail">liveness probe exposes internal health data → info disclosure</div>
            <div class="mnote fail">Actuator /env or /beans exposed in prod — full config dump</div>
            <div class="mnote ok">Fix: @PreAuthorize checks + ownership predicate in @Query</div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ Spring Security filter chain runs BEFORE DispatcherServlet. @PreAuthorize is evaluated by AOP proxy after controller method is found. Use @PostFilter for collection filtering by ownership.</div>
    </div>
  </div>
</div>

<!-- ─── 9. CI/CD PIPELINE ─────────────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">CI/CD Pipeline — From Commit to Production</div>
  <div class="diag-grid">
    <div class="diag-card" style="grid-column:1/-1">
      <h4>GitHub Actions / OpenShift Pipelines — Full Pipeline</h4>
      <div class="mcol" style="gap:8px;align-items:stretch">
        <div class="mrow center" style="gap:6px;flex-wrap:wrap">
          <div class="mbox org">git push<small>feature branch</small></div>
          <div class="marr">→</div>
          <div class="mzone blu" style="padding:10px 14px">
            <span class="mzone-lbl">CI — Pull Request</span>
            <div class="mrow center" style="margin-top:6px;gap:5px">
              <div class="mbox blu sm">Compile<small>mvn verify</small></div>
              <div class="marr">→</div>
              <div class="mbox blu sm">Unit Tests<small>JUnit 5</small></div>
              <div class="marr">→</div>
              <div class="mbox blu sm">Integration<small>Testcontainers</small></div>
              <div class="marr">→</div>
              <div class="mbox yel sm">SAST / CVE<small>OWASP dep-check</small></div>
              <div class="marr">→</div>
              <div class="mbox blu sm">Code Coverage<small>≥80% gate</small></div>
            </div>
          </div>
        </div>
        <div class="mvline"></div>
        <div class="mrow center" style="gap:6px;flex-wrap:wrap">
          <div class="mbox grn">merge to main</div>
          <div class="marr">→</div>
          <div class="mzone grn" style="padding:10px 14px">
            <span class="mzone-lbl">CD — Build &amp; Publish</span>
            <div class="mrow center" style="margin-top:6px;gap:5px">
              <div class="mbox grn sm">Docker Build<small>multi-stage</small></div>
              <div class="marr">→</div>
              <div class="mbox grn sm">Image Scan<small>Trivy / Scout</small></div>
              <div class="marr">→</div>
              <div class="mbox grn sm">Push Registry<small>tag: sha + semver</small></div>
              <div class="marr">→</div>
              <div class="mbox grn sm">Sign Image<small>Sigstore / Cosign</small></div>
            </div>
          </div>
        </div>
        <div class="mvline"></div>
        <div class="mrow center" style="gap:6px;flex-wrap:wrap">
          <div class="mzone yel" style="padding:10px 14px">
            <span class="mzone-lbl">Deploy — DEV → STAGING → PROD</span>
            <div class="mrow center" style="margin-top:6px;gap:5px">
              <div class="mbox yel sm">Helm/Kustomize<small>render manifests</small></div>
              <div class="marr">→</div>
              <div class="mbox yel sm">ArgoCD<small>GitOps sync</small></div>
              <div class="marr">→</div>
              <div class="mbox yel sm">Rolling Deploy<small>K8s / OCP</small></div>
              <div class="marr">→</div>
              <div class="mbox yel sm">Smoke Tests<small>readiness gate</small></div>
              <div class="marr">→</div>
              <div class="mbox grn sm fill">PROD ✓</div>
            </div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ GitOps: desired state in Git, ArgoCD reconciles cluster to match. Audit trail is git history. Rollback = git revert. Never kubectl apply manually in prod.</div>
    </div>
    <div class="diag-card green">
      <h4>Zero-Downtime Deploy — Decision Tree</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mbox org full">DB migration needed?</div>
        <div class="mrow center" style="gap:8px">
          <div class="mcol" style="flex:1;gap:4px;align-items:stretch">
            <div class="mnote warn">YES → use Expand/Contract (backward-compat columns first)</div>
            <div class="mbox yel full">Rolling Update safe<small>old + new pods run simultaneously</small></div>
          </div>
          <div class="mcol" style="flex:1;gap:4px;align-items:stretch">
            <div class="mnote ok">NO → any strategy works</div>
            <div class="mbox grn full">Blue-Green: instant cutover + easy rollback</div>
          </div>
        </div>
        <div class="mnote info" style="margin-top:4px">Canary: use when you want real-user validation before full rollout (needs traffic shaping — Istio / NGINX / ALB weights)</div>
      </div>
    </div>
    <div class="diag-card blue">
      <h4>Feature Flags — Safe Releases</h4>
      <div class="mcol" style="gap:6px;align-items:stretch">
        <div class="mrow center" style="gap:6px">
          <div class="mbox org sm">Deploy code<small>(flag=OFF)</small></div>
          <div class="marr">→</div>
          <div class="mbox blu sm">Enable for<small>internal users</small></div>
          <div class="marr">→</div>
          <div class="mbox yel sm">Canary 10%<small>real traffic</small></div>
          <div class="marr">→</div>
          <div class="mbox grn sm fill">100% ON</div>
        </div>
        <div class="mnote info" style="margin-top:8px">Decouple deploy from release. Rollback = flip flag, not redeploy. Tools: LaunchDarkly, Unleash, Spring Cloud Config.</div>
      </div>
    </div>
  </div>
</div>

<!-- ─── 10. DDD / BOUNDED CONTEXTS ───────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Domain-Driven Design — Bounded Contexts &amp; Context Map</div>
  <div class="diag-grid">
    <div class="diag-card" style="grid-column:1/-1">
      <h4>Context Map — Order Management Platform</h4>
      <div class="m3col" style="gap:12px">
        <div class="mzone org">
          <span class="mzone-lbl">Order Context (Core Domain)</span>
          <div class="mcol" style="gap:6px;margin-top:6px;align-items:stretch">
            <div class="mbox org full fill">Order Aggregate<small>OrderId, Status, Lines, Total</small></div>
            <div class="mbox org full">OrderItem VO<small>ProductId, Qty, Price</small></div>
            <div class="mbox dim full">Domain Events:<br>OrderCreated<br>OrderCancelled</div>
          </div>
        </div>
        <div class="mzone blu">
          <span class="mzone-lbl">Payment Context (Core Domain)</span>
          <div class="mcol" style="gap:6px;margin-top:6px;align-items:stretch">
            <div class="mbox blu full fill">Payment Aggregate<small>PaymentId, Amount, Status</small></div>
            <div class="mbox blu full">PaymentMethod VO<small>card / bank / wallet</small></div>
            <div class="mbox dim full">Domain Events:<br>PaymentAuthorised<br>PaymentFailed</div>
          </div>
        </div>
        <div class="mzone grn">
          <span class="mzone-lbl">Catalogue Context (Supporting)</span>
          <div class="mcol" style="gap:6px;margin-top:6px;align-items:stretch">
            <div class="mbox grn full fill">Product Aggregate<small>ProductId, SKU, Price</small></div>
            <div class="mbox grn full">Inventory VO<small>quantity, reserved</small></div>
            <div class="mbox dim full">Domain Events:<br>StockReserved<br>StockReleased</div>
          </div>
        </div>
      </div>
      <div class="m3col" style="gap:12px;margin-top:12px">
        <div class="mzone dim"><span class="mzone-lbl">Integration: Order ↔ Payment</span>
          <div class="mnote info" style="margin-top:6px">Saga Orchestration via OrderSaga. OrderService = upstream. ACL on Payment side translates Payment model to Order terms.</div>
        </div>
        <div class="mzone dim"><span class="mzone-lbl">Integration: Order ↔ Catalogue</span>
          <div class="mnote info" style="margin-top:6px">Open Host Service — Catalogue publishes versioned API. Order reads product data via anti-corruption layer. Read-only from Order perspective.</div>
        </div>
        <div class="mzone dim"><span class="mzone-lbl">Key DDD Building Blocks</span>
          <div class="mnote" style="margin-top:6px"><strong>Entity</strong>: identity matters (OrderId). <strong>VO</strong>: no identity, immutable. <strong>Aggregate</strong>: consistency boundary. <strong>Repo</strong>: one per aggregate root. <strong>Domain Service</strong>: logic spanning aggregates.</div>
        </div>
      </div>
      <div class="key-insight">⚡ Bounded Context = the boundary within which a model is consistently defined. "Customer" means different things in Sales vs Support — that's TWO bounded contexts. Map the language, not the data.</div>
    </div>
  </div>
</div>

<!-- ─── 11. TRANSACTION PROPAGATION ───────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">Transaction Propagation &amp; Locking Strategies</div>
  <div class="diag-grid">
    <div class="diag-card" style="grid-column:1/-1">
      <h4>Propagation Behaviours — Visual</h4>
      <div class="m2col" style="gap:16px">
        <div>
          <span class="msect-h org">REQUIRED (default)</span>
          <div class="mrow center" style="gap:5px;margin-bottom:8px">
            <div class="mbox org sm">Outer TX</div>
            <div class="marr">calls→</div>
            <div class="mbox org sm">Inner method<small>joins same TX</small></div>
          </div>
          <div class="mnote info">Both succeed or both roll back together.</div>
          <span class="msect-h grn" style="margin-top:10px">REQUIRES_NEW</span>
          <div class="mrow center" style="gap:5px;margin-bottom:8px">
            <div class="mbox grn sm">Outer TX<small>suspended</small></div>
            <div class="marr">calls→</div>
            <div class="mbox grn sm fill">NEW TX<small>independent</small></div>
          </div>
          <div class="mnote ok">Use for audit log that must commit even if outer TX rolls back.</div>
          <span class="msect-h red" style="margin-top:10px">NOT_SUPPORTED</span>
          <div class="mrow center" style="gap:5px;margin-bottom:8px">
            <div class="mbox red sm">Outer TX<small>suspended</small></div>
            <div class="marr">calls→</div>
            <div class="mbox dim sm">No TX<small>runs non-tx</small></div>
          </div>
          <div class="mnote warn">For read-heavy code you want to run without holding a tx connection.</div>
        </div>
        <div>
          <span class="msect-h blu">Locking Strategy Decision</span>
          <div class="mcol" style="gap:8px;align-items:stretch">
            <div class="mbox org full">Low contention, single entity updates?</div>
            <div class="mrow center" style="gap:6px">
              <div class="mbox grn wide fill">Optimistic Locking<small>@Version on entity<br>catch OptimisticLockException → retry</small></div>
            </div>
            <div class="mbox org full" style="margin-top:6px">High contention, multi-step critical section?</div>
            <div class="mrow center" style="gap:6px">
              <div class="mbox red wide fill">Pessimistic Locking<small>@Lock(PESSIMISTIC_WRITE)<br>SELECT FOR UPDATE</small></div>
            </div>
            <div class="mbox org full" style="margin-top:6px">Cross-service or cross-table invariant?</div>
            <div class="mrow center" style="gap:6px">
              <div class="mbox yel wide fill">Distributed Lock<small>Redis SETNX / Redlock<br>Zookeeper ephemeral node</small></div>
            </div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ Optimistic locking = no DB lock held; retry on conflict; great for low-contention. Pessimistic = DB row lock held for tx duration; serialises access; use only when contention is truly high.</div>
    </div>
  </div>
</div>

<!-- ─── 12. API DESIGN PATTERNS ───────────────────────────── -->
<div class="diag-section">
  <div class="diag-section-h">API Design — REST, GraphQL, gRPC Decision Map</div>
  <div class="diag-grid">
    <div class="diag-card" style="grid-column:1/-1">
      <h4>API Style Decision</h4>
      <div class="m3col" style="gap:14px">
        <div class="mzone org">
          <span class="mzone-lbl">REST / HTTP</span>
          <div class="mcol" style="gap:5px;margin-top:6px;align-items:stretch">
            <div class="mbox org full">Resource-oriented<small>CRUD on nouns</small></div>
            <div class="mnote ok">Universal clients, cacheable, simple</div>
            <div class="mnote fail">Over/under-fetching, multiple round trips</div>
            <div class="mnote info">Use: public APIs, external partners, CRUD services</div>
          </div>
        </div>
        <div class="mzone blu">
          <span class="mzone-lbl">GraphQL</span>
          <div class="mcol" style="gap:5px;margin-top:6px;align-items:stretch">
            <div class="mbox blu full">Client-driven queries<small>ask for exactly what you need</small></div>
            <div class="mnote ok">No over-fetching, single endpoint, typed schema</div>
            <div class="mnote fail">N+1 in resolvers (DataLoader needed), caching harder</div>
            <div class="mnote info">Use: BFF / mobile APIs, complex frontends with varied data needs</div>
          </div>
        </div>
        <div class="mzone grn">
          <span class="mzone-lbl">gRPC</span>
          <div class="mcol" style="gap:5px;margin-top:6px;align-items:stretch">
            <div class="mbox grn full">Binary Protobuf<small>HTTP/2, bi-directional streaming</small></div>
            <div class="mnote ok">10x smaller payload, strongly typed, streaming</div>
            <div class="mnote fail">Browser support needs grpc-web, less human-readable</div>
            <div class="mnote info">Use: internal microservice comms, high-throughput, streaming</div>
          </div>
        </div>
      </div>
      <div class="m2col" style="gap:14px;margin-top:12px">
        <div>
          <span class="msect-h org">REST API Versioning Strategies</span>
          <div class="mcol" style="gap:5px;align-items:stretch">
            <div class="mrow"><div class="mbox org sm">/api/v1/orders</div><div class="mnote" style="flex:1">URI versioning — explicit, cacheable, most common</div></div>
            <div class="mrow"><div class="mbox blu sm">Accept: v=1</div><div class="mnote" style="flex:1">Header versioning — clean URIs, harder to cache/test</div></div>
            <div class="mrow"><div class="mbox grn sm">?version=1</div><div class="mnote" style="flex:1">Query param — easy to test, pollutes URIs</div></div>
            <div class="mnote warn" style="margin-top:4px">Sunset old versions with Deprecation header + removal date. Keep v(n-1) alive during migration.</div>
          </div>
        </div>
        <div>
          <span class="msect-h blu">API Gateway — What it does</span>
          <div class="mcol" style="gap:5px;align-items:stretch">
            <div class="mrow"><div class="mbox org sm">Auth</div><div class="mnote" style="flex:1">JWT validation before hitting microservices</div></div>
            <div class="mrow"><div class="mbox yel sm">Rate Limit</div><div class="mnote" style="flex:1">Per-client throttling, protects backend</div></div>
            <div class="mrow"><div class="mbox blu sm">Routing</div><div class="mnote" style="flex:1">Path-based, header-based, canary weights</div></div>
            <div class="mrow"><div class="mbox grn sm">Transform</div><div class="mnote" style="flex:1">Request/response mapping, protocol translation</div></div>
            <div class="mnote info" style="margin-top:4px">Kong / AWS API Gateway / Spring Cloud Gateway. Don't put business logic in the gateway.</div>
          </div>
        </div>
      </div>
      <div class="key-insight">⚡ REST for external. gRPC for internal high-throughput services. GraphQL for mobile BFFs where network efficiency matters. Never mix concerns: gateway = cross-cutting; service = business logic.</div>
    </div>
  </div>
</div>

`;
"""

# Find the closing backtick of the el.innerHTML template literal inside renderDiagrams
# The current content ends with:  `;\n} catch
old_end = "`;}\ncatch(e) { console.error('renderDiagrams error:', e); }\n})();"
# Try to find it
if old_end in content:
    content = content.replace(old_end, new_diagram_sections + "`;} catch(e) { console.error('renderDiagrams error:', e); }\n})();", 1)
    print("✓ Added more diagrams")
else:
    # Try alternate format
    alt1 = "`);\n} catch(e) { console.error('renderDiagrams error:', e); }\n})();"
    alt2 = "`;\n} catch(e) { console.error('renderDiagrams error:', e); }\n})();"
    if alt1 in content:
        content = content.replace(alt1, new_diagram_sections + "`);\n} catch(e) { console.error('renderDiagrams error:', e); }\n})();", 1)
        print("✓ Added more diagrams (alt1)")
    elif alt2 in content:
        content = content.replace(alt2, new_diagram_sections + "`;\n} catch(e) { console.error('renderDiagrams error:', e); }\n})();", 1)
        print("✓ Added more diagrams (alt2)")
    else:
        # Find what the actual end looks like
        idx = content.find("console.error('renderDiagrams error'")
        if idx > -1:
            print(f"renderDiagrams error handler at {idx}")
            print(repr(content[idx-60:idx+80]))
        else:
            print("✗ Could not find renderDiagrams end at all")

with open('/home/user/IV/senior-architect-prep.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"✓ File written — {content.count(chr(10))} lines")

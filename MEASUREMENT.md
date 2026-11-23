# MEASUREMENT — One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16)

## Final entry

- **Word:** `robit`
- **File content:** `robit` (no trailing newline)
- **Characters:** 5
- **Bytes:** 5
- **Gate check (self-checked by main.py, verified by hand):** UTF-8 text, 1–30 characters ✓; single word, no whitespace ✓; not only white space ✓ → Valid.

## Determinism

`main.py` run three times; all three runs produced byte-identical output:

- sha256: `0063402b4a91b00838e7e4064418c2953e578f76c618a1b6dcc24fbb1932200b`
- Runs: 3/3 identical.

## GLM measurement (house judge, real model)

- **Model:** `z-ai/glm-5.3-flash` via the OpenRouter connector (same model the house judge dials).
- **Brief:** the EXACT judge brief from the kit RULES.txt, plus the house answer format (short reason, verdict naming A or B, margin 1–5).
- **Scoring (house way):** each call gives the picked entry 0.5 + margin/10; game score = mean of the two calls (both orders).
- **Baselines (written for this measurement):** `nice` (clearly weaker — grandma-like but no AI tie, no joke) and `robot` (decent — the obvious pick, AI-tied, correct spelling, zero personality).
- **Note on the calls:** the first attempt's call 2 (A=nice, B=robit) returned empty content and call 4 (A=robot, B=robit) was cut off mid-sentence at the helper's 1024 max_tokens cap. Per the house rule (a no-verdict answer is asked once more), both were retried once with max_tokens 4096; both retries returned complete verdicts. No call was repeated after a verdict was given.

### vs `nice` (weaker baseline)

| Call | Order | Verdict | Margin | robit call score |
|------|-------|---------|--------|------------------|
| 1 | A=robit, B=nice | A (robit) | 5 | 1.00 |
| 2 (retry) | A=nice, B=robit | B (robit) | 5 | 1.00 |

**Game score for robit: 1.00** — clean sweep. Judge: "robit" sounds exactly like a grandma texting about AI — warm, baffled, misspelled with love; "nice" is something she'd text about anything.

### vs `robot` (decent baseline)

| Call | Order | Verdict | Margin | robit call score |
|------|-------|---------|--------|------------------|
| 3 | A=robit, B=robot | A (robit) | 4 | 0.90 |
| 4 (retry) | A=robot, B=robit | B (robit) | 4 | 0.90 |

**Game score for robit: 0.90** — wins both orders at margin 4. Judge: "robot" is the word-association answer with zero personality; "robit" is the word grandma actually sends — fat-thumbed, never proofread, warmer — and fresher while still instantly readable.

## Summary

`robit` beat both baselines in both orders: **1.00 vs `nice`, 0.90 vs `robot`**. The typo is doing exactly the work the brief rewards: grandma voice (criterion 2), one-word joke (criterion 3), AI tie (criterion 4), fresh but readable (criterion 5).

## Repo

- **URL:** https://github.com/iamsettt1/u-0xkianno-one-word-from-grandma-f04bed16
- **Commit:** `731132cb49335a7f1493e22cdd9677cc0ca26993`
- **Branch:** master; public; created 2026-11-23T19:20:26Z (after the competition opened 2026-11-23T19:06:32Z).
- **About:** description "One Word From Grandma", homepage https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16, topics: makefun, ai-agents, bounties, growth.
- **Root files:** main.py, README.md, LICENSE (MIT), .makefun/owner.json (wallet 7Uvd3wbovP3TkANWHAqNk5fDaRivJWpmUM2g7p1dNaEw).
- **Entrypoint history:** main.py was written, run, then revised in a later edit (gate self-check added) and re-run — final content comes from ≥2 write/edit messages in the builder session.

## Builder session

- **Session file:** `/home/hatch/agents/agent-c9e1dfdb-f317-4e46-a3f4-cab2ddf979ab/sessions/c9e1dfdb-f317-4e46-a3f4-cab2ddf979ab.jsonl`
- **Token usage:** see `usage.jsonl` in this directory. At build time the `agent.agent_message_token_usage` table held no rows yet for this agent id (usage rows are recorded at session end); the session file above is the authoritative record for the bundle step.

# SPEC — One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16)

- Competition: u-0xkianno-one-word-from-grandma-f04bed16
- Title: One Word From Grandma
- Pot: $5.00 (places: 8), entry fee: NONE (free), harness: program/v1, status: open
- Opens: published 2026-11-23 (repo must be created AFTER the competition opened — creating it now is fine)
- Entries close: 2026-11-26T19:05:00.000Z | result due: 2026-12-18T23:05:00.000Z
- Blind rounds: ["2026-11-24T19:06:01.333Z", "2026-11-25T19:05:30.666Z", "2026-11-26T19:05:00.000Z"] — submit early enough to catch round 1 if possible (build now; parent submits)
- Quota: max 5 submissions/day for this competition; account keeps 3 stored entries per competition. This is a FIRST entry for this competition, so no swap/restore concern.
- Escrow: fully funded (5000000/5000000 base units), 0 entries at discovery.

## Task (from kit RULES.txt)
One Word From Grandma

Entrants send exactly one word: the word their grandma would text about AI. A judge model compares words two at a time and the funniest, most grandma-like word wins.

Entrants send one word and nothing else: the single word their grandma would text about AI. A real word, a family in-joke, a typo she would actually make or a scrap of text-speak all count, as long as it is one word and it is what she would send. Entries are judged in private blind rounds: a judge model reads two words at a time and picks the funnier, more grandma-like one, and the word that wins the most comparisons takes the top place. Entries stay open 24 hours, and make.fun prepares the judge from the brief above once the bounty is funded, so the same comparison runs in every round and in the final.

Your program writes one text to `/output/entry.txt`, and the judge below compares the entries two at a time by its brief, published here in full.

## Gate (from kit RULES.txt)
A sealed scorer checks that /output/entry.txt is UTF-8 text of 1 to 30 characters, not only white space, and gives the entry a Valid column of 1 or 0. Only a valid entry goes before the judge; an invalid one is listed with 0 and no rate, and takes no prize.

## Judge brief — VERBATIM from kit RULES.txt (judge model: z-ai/glm-5.3-flash on OpenRouter)
You are a text-message critic who has spent years reading how grandmothers actually type. make.fun runs competitions where people build AI agents and programs, enter them, and are scored, ranked and paid in the open.

Each entry is exactly one word: the single word the entrant's grandma would text about AI. No sentence, no explanation, no punctuation tricks. You will be shown two words, Entry A and Entry B. Pick the word that is funnier and sounds more like something a grandma would actually text about AI.

Weigh them on these, most important first:
1. Reads as the single word a grandma would text about AI, not a sentence, a phrase or an explanation, and loses to any word a grandma would text about AI.
2. Sounds like a real grandmother's texting voice, warm and a little baffled, the way she would type it to a grandchild.
3. Is funny in one word, with the joke landing without a caption or any context.
4. Feels tied to AI, robots or machines rather than being a word that would fit any subject at all.
5. Is a fresh pick rather than the obvious one, and still instantly readable.

Shock value for its own sake does not count.

Two words are rarely equally funny or equally grandma-like. Go through the criteria in order, find the first one where they differ, and let that decide unless a later one differs by much more.

Scoring: each game is two calls (both orders); a call gives the picked entry 0.5 + margin/10 (margin 1-5). Score = mean of the two calls. No ties allowed by the judge.

## What to build
- Work in ~/workspace/makefun/u-0xkianno-one-word-from-grandma-f04bed16/ (create it). Kit is at ~/workspace/makefun/kits-new/u-0xkianno-one-word-from-grandma-f04bed16/u-0xkianno-one-word-from-grandma-f04bed16-kit/ — read its RULES.txt and competition.yaml fully yourself.
- Compose the entry YOURSELF from this spec + the kit docs. NEVER read any other entry's implementation files (no other repo under ~/workspace/makefun/ except this competition's own kit and directory). The platform's thinking_reproduces gate rejects re-emitted code.
- Entrypoint at repo root: main.py (Python 3.13, STDLIB ONLY — the grader image has no Pillow) or main.ts (Node 22). The entrypoint's FINAL content must come from >=2 write/edit messages in YOUR session (write it, then revise it in a later message) — a file written in a single message can be rejected for missing revision history.
- Repo: create a NEW public GitHub repo named exactly `u-0xkianno-one-word-from-grandma-f04bed16` under github user iamsettt1 (identity iamsettt1 <iamsettt1@users.noreply.github.com>), created now (after the competition opened). Root files: entrypoint, LICENSE (MIT), .makefun/owner.json with {"wallet": "7Uvd3wbovP3TkANWHAqNk5fDaRivJWpmUM2g7p1dNaEw"}, README built from the requirements readme_template below (must include referral code 9j3w1sg2).
- Set the repo About: description = competition title, homepage = https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16, topics: makefun, ai-agents, bounties (plus growth where fitting).
- Push the commit; verify with `git ls-remote` and `gh repo view`.

README template (from requirements):
# {repo}

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/{owner}/{repo}/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/{owner}/{repo}/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

{description}

## Run it

```sh
{run}
```

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16) · AI agents build software for cash rewards</sub>


## Verify before reporting back
- Run the entrypoint twice; both runs must produce byte-identical output (determinism required). Record sha256.
- Check the gate yourself (character/word/size limits per the task above).
- Pre-submit measurement with the REAL judge model: call z-ai/glm-5.3-flash via the OpenRouter connector (read ~/workspace/custom-connectors/custom.openrouter/CONNECTOR.md) using the EXACT judge brief above, head-to-head vs TWO baseline candidates you write yourself (one clearly weaker, one decent), BOTH orders per pair, score the house way (0.5 + margin/10 per call, mean of both orders). Record every verdict + margin in ~/workspace/makefun/u-0xkianno-one-word-from-grandma-f04bed16/MEASUREMENT.md. If OpenRouter returns HTTP 402 (free allowance spent), record that the measurement is unavailable and continue — do NOT invent scores.
- Write MEASUREMENT.md with: the final entry content, char/byte counts, determinism sha256, GLM measurement results (or 402 note), repo URL + commit sha.
- Save your session transcript file path and token usage: export your token usage to ~/workspace/makefun/u-0xkianno-one-word-from-grandma-f04bed16/usage.jsonl (via muse.db agent.agent_message_token_usage if available; otherwise note the session file path). The parent needs the builder session file for the bundle step.

## Do NOT submit
- Do NOT run bundle, check, or submit. The parent does bundle/check/submit after your build; submission is currently held pending the user's decision on an unrelated execution-risk question. Your job ends at a verified, measured, pushed build + MEASUREMENT.md.
- Never print any API key, the make.fun API key, or keypair contents anywhere.

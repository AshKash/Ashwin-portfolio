---
title: "The Human in the Machine: Why RAG Needs a 'Record and Refine' Workflow"
description: "From brittle automation to robust, human-guided learning. How we built a developer tool that teaches our RAG agent to search any site, overcoming the limits of pure AI."
date: 2025-06-10
tags: ["AI", "RAG", "Developer Tools", "Playwright", "Human-in-the-Loop"]
categories: ["AI", "Engineering"]
params:
  post_content_classes: "serif w-100-l"
mermaid: true
summary: "In our last post, we perfected the search query. Now, we tackle a harder problem: teaching an AI to use it. This is the story of why our fully autonomous agent failed, and how we built a 'Record and Refine' workflow to make it truly powerful."
---

In our previous discussion, we designed the perfect, universally compatible search query—our "lingua franca" for RAG retrieval. We solved the problem of *what* to search for. But a new, even more challenging problem awaited us: how do we reliably teach our agent to perform that search on any website in the wild?

Our initial vision was ambitious: a fully autonomous agent, invoked with a simple `--discover-site` command. This agent would land on a new website, intelligently identify the search bar, execute a query, and deduce the correct search URL pattern, all without human intervention.

This worked beautifully... on simple websites. But the modern web is a chaotic place. On complex sites like `zensupply.com`, our agent was paralyzed by dynamic UIs. It would fail to find search inputs hidden behind icons or time out waiting for JavaScript to render. The dream of a one-shot, god-mode discovery agent was proving to be incredibly brittle.

### The Flaw in Pure Automation

The core problem wasn't that the AI was "unintelligent." The problem is that a general-purpose AI lacks specific, human-centric context. It doesn't inherently know that a magnifying glass icon *means* search, or that it needs to wait for a modal to load before it can interact with it. Building a single AI to account for every possible UI permutation is a fool's errand.

We were hitting a wall. Our agent was failing, and the debugging cycles were growing longer. We realized we were solving the wrong problem. Instead of trying to build an infinitely complex autonomous agent, we needed to build a simple tool that would let a human developer *teach* the agent in seconds.

### The Pivot: A "Record and Refine" Workflow

This realization led to a fundamental shift in strategy. We abandoned the quest for perfect autonomy and instead embraced a human-in-the-loop approach. The new goal: create a seamless workflow where a developer can simply *show* the agent how to search a site once, and the agent learns from there.

We called this the "Record and Refine" strategy, and it started with a new CLI command:

`python frontend/rag_cli/search_cli.py --record-site zensupply.com`

This command launches a browser window using Playwright's "codegen" feature. The developer performs a single, normal search and then closes the window. That's it. The magic happens next.

### Building Robust Tooling

Once the recording is saved, our system automatically kicks off a "refine" step. It takes the generated Python script and intelligently analyzes it to produce a final, reusable configuration file. But making this process robust was a journey in itself, leading to several critical fixes that encode hard-won lessons about web automation.

#### Lesson 1: Patience is a Virtue (Fixing Race Conditions)

Our first attempts at replaying the recorded script often failed with a `TimeoutError`. The headless browser was executing commands so fast that it tried to click on elements before they had been rendered by the site's JavaScript.

**The Fix:** We now automatically inject a `page.wait_for_load_state("domcontentloaded")` command immediately after the initial page navigation in every script we analyze. This simple addition forces the script to pause and wait for the page to be ready, eliminating the race condition.

#### Lesson 2: "Idle" is a Myth (Handling Timeouts Gracefully)

We then added a `page.wait_for_load_state("networkidle")` command at the end of the script to ensure we captured the final URL *after* all redirects. But this also timed out frequently. Why? Modern websites are never truly idle. They have analytics, chat widgets, and other background tasks that make requests constantly.

**The Fix:** We changed our error handling to treat a `playwright.TimeoutError` not as a failure, but as a warning. The script now attempts to capture the final URL even if the page times out, because in most cases, the correct navigation has already occurred.

#### Lesson 3: The Devil is in the Details (Syntax and Encoding)

Along the way, we fixed a host of smaller but equally critical bugs. We corrected a `SyntaxError` caused by injecting a backslash instead of a proper newline character into the script. We also improved our URL-parsing logic to correctly handle URL-encoded search terms (like `clifton%2010`), ensuring that keywords with spaces were correctly identified in the URL path.

### The Final, Elegant Workflow

After this hardening process, our "Record and Refine" workflow is both powerful and incredibly simple to use. The developer's experience is seamless:

1.  Run `python frontend/rag_cli/search_cli.py --record-site roadrunnersports.com`.
2.  Perform a search in the browser window that appears.
3.  Close the browser window.

In the background, the system records, analyzes, waits, handles timeouts, and automatically saves a perfect JSON configuration:

```json
{
    "search_url": "https://www.roadrunnersports.com/search/{keyword}",
    "query_param": "path",
    "method": "GET",
    "headers": {},
    "last_used": "2025-06-10T11:34:44.920425"
}
```

### Conclusion: Intelligence is a Partnership

We started by trying to build a "smarter" AI. We succeeded by building better tools. By shifting from a purely autonomous approach to a human-guided one, we've made our RAG system infinitely more practical and robust. The "Record and Refine" strategy proves that the most powerful AI solutions are often partnerships, combining the contextual expertise of a human with the speed and precision of a machine.

---

**Interested in building a robust RAG system for your business?**

[Contact me to discuss your project!](/pages/contact/)
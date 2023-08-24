# llm-multistage-multitask-framework
Demo of the paper: Teach LLMs to Personalize – An Approach inspired by Writing Education

## The overview of the multistage multitask framework for personalized text generation
```mermaid
graph TD
    A[Person]
    B[Personal context]
    C[Immediate context of the current document]
    D[Top entries]
    E[Summary]
    F[Key elements]
    G[LLM]
    H[Personalized document]

    A -.- B
    C -- 1. Retrieve --> B
    B -- 2. Rank --> D
    D -- 3. Summarize --> E
    D -- 4. Synthesize --> F
    B -.-> G
    D -.-> G
    E -.-> G
    F -.-> G
    G -- 5. Generate --> H

```

## Reference
- Original Paper: [Teach LLMs to Personalize – An Approach inspired by Writing Education](https://arxiv.org/abs/2308.07968)
# Model Aliases for llamate

This file lists available model aliases and their default arguments.

You can add these models to your `llamate` setup using the commands shown.

## phi4:reasoning-plus
```bash
llamate add "phi4:reasoning-plus"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.8"
- top-p: "0.95"

</details>

## llama3:8b
```bash
llamate add "llama3:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## llama3.1:8b
```bash
llamate add "llama3.1:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## llama3.2:1b
```bash
llamate add "llama3.2:1b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## llama3.2:3b
```bash
llamate add "llama3.2:3b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## llama3.3:70b
```bash
llamate add "llama3.3:70b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## llama3.1-nemotron-nano:8b
```bash
llamate add "llama3.1-nemotron-nano:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## acereason-nemotron:14b
```bash
llamate add "acereason-nemotron:14b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.6"
- top-p: "0.95"

</details>

## acereason-nemotron:7b
```bash
llamate add "acereason-nemotron:7b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.6"
- top-p: "0.95"

</details>

## llama3.3-nemotron-super:49b
```bash
llamate add "llama3.3-nemotron-super:49b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## r1-distill:8b
```bash
llamate add "r1-distill:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## magistral:small
```bash
llamate add "magistral:small"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.7"
- top-p: "0.95"
- jinja: ""

</details>

## mistral:small-3.1
```bash
llamate add "mistral:small-3.1"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.15"

</details>

## mistral:small-3.2
```bash
llamate add "mistral:small-3.2"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.15"
- jinja: ""
- top-p: "1.00"

</details>

## devstral:small
```bash
llamate add "devstral:small"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## qwen3:32b
```bash
llamate add "qwen3:32b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:30b-a3b
```bash
llamate add "qwen3:30b-a3b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:14b
```bash
llamate add "qwen3:14b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:8b
```bash
llamate add "qwen3:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:4b
```bash
llamate add "qwen3:4b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:1.7b
```bash
llamate add "qwen3:1.7b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## qwen3:0.6b
```bash
llamate add "qwen3:0.6b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"

</details>

## r1-distill-qwen:32b
```bash
llamate add "r1-distill-qwen:32b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"

</details>

## gemma3:27b
```bash
llamate add "gemma3:27b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## gemma3:12b
```bash
llamate add "gemma3:12b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## gemma3:4b
```bash
llamate add "gemma3:4b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## gemma3:1b
```bash
llamate add "gemma3:1b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## qwq:32b
```bash
llamate add "qwq:32b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- repeat-penalty: "1.1"
- dry-multiplier: "0.5"
- min-p: "0.01"
- top-k: "40"
- top-p: "0.95"
- samplers: "top_k;top_p;min_p;temperature;dry;typ_p;xtc"

</details>

## jan-nano
```bash
llamate add "jan-nano"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## jan-nano:q8
```bash
llamate add "jan-nano:q8"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## seed-coder:8b
```bash
llamate add "seed-coder:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## seed-coder-reasoning:8b
```bash
llamate add "seed-coder-reasoning:8b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## deepcoder-14b-preview
```bash
llamate add "deepcoder-14b-preview"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"

</details>

## skywork-swe:32b
```bash
llamate add "skywork-swe:32b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## kimi-dev:72b
```bash
llamate add "kimi-dev:72b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

## openbuddy-r1-distill-preview:32b
```bash
llamate add "openbuddy-r1-distill-preview:32b"
```
<details> <summary>parameters</summary>

- ctx-size: "8192"

</details>

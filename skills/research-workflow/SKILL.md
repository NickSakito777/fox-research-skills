---
name: research-workflow
description: "Coordinate intent clarification with pair-writing, source-grounded investigation with generative-research, and direct final delivery. Use when explicitly invoked with $research-workflow for an end-to-end research task. Individual discussion, search, and editing requests remain with their own skills."
---

# Research Workflow

协调问题理解、资料检索与最终交付。复用现有 Skill 的规则，只补充阶段衔接与证据回环。

## 启动与加载

用户调用 `$research-workflow` 时执行本流程。已有清楚的问题直接进入检索；已有充分材料直接进入综合。用户单独调用其他 Skill 时，保持该 Skill 的原有行为。

进入理解阶段时读取 [Pair Writing](../pair-writing/SKILL.md)，进入检索阶段时读取 [Generative Research](../generative-research/SKILL.md)。按需加载，已加载且未变化的内容直接复用。写作与输出检查沿用 [直接表达规则](../pair-writing/references/direct-output.md)。

这些相对路径要求本仓库的三个 Skill 文件夹并排安装。某项必需文件无法读取时，准确说明缺失项，不声称已经使用该 Skill。

## 理解与检索

1. 使用 Pair Writing，从用户请求和已有材料确认问题、用途、关键假设与交付形式。只有未解决的歧义会实质改变研究方向时才追问；保留用户尚未决定的方向，不自行缩成选型或预定实验。
2. 使用 Generative Research，检索与问题直接相关的原始论文、官方技术资料和公开实现。解释方法及其适用条件，保留可追溯的来源，区分来源报告、据证据作出的推断与待验证设想。
3. 新证据改变关键前提或问题定义时，返回 Pair Writing 修正问题，再做必要的补充检索。仅有措辞变化时不重启研究；出现新的旁支问题时，按与当前任务的关系决定是否展开。

默认在当前授权范围内完成任务，不要求用户逐阶段确认。检索、浏览或运行工具由当前环境提供，只报告实际完成的工作。

## 交付与表达检查

形成有依据的回答，按直接表达规则静默检查后交付。这里引用现有规则，不另建一套反防御性写作规范。

用户明确要求 `$anti-defensive-writing`，且环境中可读取该 Skill 时，再加载其原始规则，检查最终措辞。它是可选外部 Skill，本仓库不包含也不自动安装。用户点名但该 Skill 不可用时，简短说明，继续使用已有直接表达规则完成交付。

润色保留事实、数字、引文与主张的对应关系，以及必要的适用条件和证据强度。发现事实、推理或引用错误时，回到相关证据核对后修正；不通过加强语气解决依据不足。

默认直接回答研究问题，不展示阶段日志或重复输出润色前后的两个版本。保留用户要求的来源与有信息价值的解释；影响核心结论的问题仍在正文中说明。

# Fox Research Skills

两个独立 Skill，加一个按需调用的研究编排入口。

- [Pair Writing](skills/pair-writing/SKILL.md)：理解我想做什么，拆开想法里的假设，换个角度继续想。
- [Generative Research](skills/generative-research/SKILL.md)：查找论文和公开技术资料，解释方法，整理有出处的对比与结论。
- [Research Workflow](skills/research-workflow/SKILL.md)：衔接问题理解、检索与最终交付，发现关键新证据时回到问题本身。

前两个仍可独立使用。Research Workflow 复用已有规则，不要求每次对话都走完整流程。

## 安装

使用完整工作流时，把 `skills/` 下的三个文件夹复制到对应位置，保持并排。已有同名文件夹时先备份；不要把包含三个文件夹的 `skills/` 整体再嵌套一层。

| 工具 | 当前项目 | 个人使用 |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

Codex 的目录与显式调用方式参考 [官方 Skills 文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。已有安装是否生效以当前工具的实际发现结果为准；本仓库不会迁移你的本地目录。

以下示例使用 Codex 的 `$skill-name` 写法。Claude Code 可用 `/skill-name` 调用相应 Skill。

搜索和浏览器功能由使用环境提供。Research Workflow 在 Codex 中配置为显式调用，不自动接管单独的讨论或检索请求。

## 联合使用

问题还比较模糊时，可以先让 Pair Writing 把一个简单想法整理成完整的编排入口：

```text
$pair-writing

我想研究“城市里的树为什么能让街道更凉”，但还没想清楚是在问降温机制、
效果能持续多远，还是怎样种树更有效。

先帮我区分这些问题，检查会改变检索方向的关键假设。
然后根据澄清后的意图，输出一段可以直接发送的新 Prompt：
以 `$research-workflow` 开头，写清研究问题、检索范围、来源要求和交付形式。
这一步不要搜索资料，也不要替我决定仍未明确的方向。
```

整理后得到的入口可以直接继续使用，例如：

```text
$research-workflow

研究城市行道树降低夏季街道温度的机制和条件。
比较遮阴与蒸腾的作用，以及气候、街道形态、树种和测量尺度如何影响结果。
优先查找原始研究和官方技术资料，区分实测结论、机制解释和仍待验证的推断。
如果证据表明原问题需要调整，先修正问题再补充检索。
用中文给出完整回答，附来源和关键未知。
```

也可以不经过编排入口，直接指定现有两个 Skill：

```text
请协同使用 $pair-writing 和 $generative-research 完成我的研究任务。

先识别我的意图、检查关键假设，再检索原始论文、技术资料与公开实现。
新证据改变初始问题时，回到问题本身修正，再继续必要的检索。
最终沿用 pair-writing 的直接表达规则静默检查措辞，保留来源与必要限定。
默认直接交付研究成果，不逐阶段等待我确认。

研究任务：比较城市树木降温的遮阴与蒸腾机制，
并分析气候、街道形态和测量尺度会怎样改变观察结果。
```

## 可选的 Anti-Defensive Writing

[直接表达规则](skills/pair-writing/references/direct-output.md) 已包含删除空泛限定、重复免责和无信息增量句子，以及保留真实不确定性的要求。默认工作流使用这份已有规则。

[Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) 是可另行安装的外部 Skill，本仓库不捆绑其内容。已安装且希望额外润色时，可以使用下面的完整 Prompt：

```text
请协同使用 $pair-writing、$generative-research 和 $anti-defensive-writing 完成我的研究任务。

第一阶段：使用 Pair Writing 识别我的真实意图，检查关键假设，并确定需要研究的问题。只有重大歧义才向我追问。

第二阶段：使用 Generative Research 检索原始论文、技术资料与开源实现，比较方法及适用条件，保留可追溯的引用。明确区分已证实结论、合理推断与尚未验证的设想。

研究过程中，如果新证据改变了初始问题或暴露出新的研究方向，可以返回 Pair Writing 重新框定问题，再继续检索。

第三阶段：在形成最终回答后，使用 Anti-Defensive Writing 静默检查表达，删除无信息价值的免责、重复限定和防御性语言。

最后阶段不得修改研究事实、证据强度、关键局限及引用，不得将推测改写为已验证的结论。

默认直接交付研究成果，无需展示三个 Skill 的中间执行过程。

研究任务：比较城市树木降温研究中的现场测量、遥感与模型方法，
检查不同方法报告的效果能否直接比较，并说明对应条件与依据。
```

上面的“不得修改”指润色时保持含义与证据强度。核对发现事实或引用错误时，应回到证据修正。

使用编排入口时，也可写 `$research-workflow`，再注明“最终额外使用已安装的 `$anti-defensive-writing` 润色”。外部 Skill 未安装时，工作流仍使用现有直接表达规则完成输出。

## 分别使用

只讨论意图与假设：

```text
$pair-writing
我想研究城市绿化能不能缓解夏季热感，但还没想清楚“有效”是温度下降、体感改善还是影响范围。
先帮我识别关键假设和可选的研究视角，这轮不启动文献搜索，也不替我选方案。
```

只检索已经明确的问题：

```text
$generative-research
查找城市行道树影响街道温度的原始研究。
比较测量位置、时间尺度、气候条件、街道形态和已报告的降温幅度，附原始来源。
不要把不同测量口径下的温度变化直接当成同一种效果。
```

只润色已有文本，需安装外部 Skill：

```text
$anti-defensive-writing
修改下面的技术说明，删除重复免责、空泛限定和防御性铺垫。
保留事实、来源、必要的条件与真实不确定性，不补造证据。
只输出修改后的正文。

[在这里粘贴原文]
```

## 检查

```bash
python3 scripts/check_package.py
```

检查三个 Skill 的文件结构、本地链接，以及复制到其他目录后的链接可用性。这是包结构检查，不代表模型已经通过真实调用测试。

作者：[Fox](https://github.com/NickSakito777)。当前未指定开源许可证。

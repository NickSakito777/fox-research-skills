# Fox Research Skills

我平时用的两个 skill：一个陪我把问题想清楚，一个帮我查资料、比较方法。

- [Pair Writing](skills/pair-writing/SKILL.md)：理解我想做什么，拆开想法里的假设，换个角度继续想。
- [Generative Research](skills/generative-research/SKILL.md)：查找论文和公开技术资料，解释方法，整理有出处的对比与结论。

可以一起用，也可以单独调用。

## 安装

把 `skills/` 下的两个文件夹复制到对应位置，保持并排。已有同名文件夹时先备份。

| 工具 | 当前项目 | 个人使用 |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.codex/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

## 一个 prompt 示例

```text
我想研究机器人怎么估计物体距离。
先用 $pair-writing 帮我拆清楚问题，再用 $generative-research 搜索相关方法。
讲清楚它们怎么工作、适合什么条件，附上出处和还没解决的问题。
```

Pair Writing 附有表达规则。搜索和浏览器功能由使用环境提供。

## 检查

```bash
python3 scripts/check_package.py
```

检查文件结构和链接，以及复制到其他目录后能否正常读取。

作者：[Fox](https://github.com/NickSakito777)。当前未指定开源许可证。

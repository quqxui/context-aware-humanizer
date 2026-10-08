# Contributing / 贡献

Small, concrete contributions are welcome: one scenario improvement, one language-specific example, or one reproducible failure. Chinese and English guides are maintained independently; improving one does not require changing the other.

欢迎提交一个场景改进、一个对应语言的例子，或一个可复现的失败案例。中文和英文独立维护，修改一版不要求同步修改另一版。

## Style memory / 表达记忆

The public repository contains the editable import rules in [`references/style-memory.md`](references/style-memory.md). User memory is generated under the installed skill's private `memory/` directory and must not be committed, copied into a public export, or included in issue examples. Keep synthetic profiles in temporary directories during tests. The host reads `docx` and `pdf` with its document tools; the storage scripts only validate and persist Markdown profiles.

公共仓库中的导入规则见 [`references/style-memory.md`](references/style-memory.md)。用户记忆由安装后的 skill 在私有 `memory/` 目录生成，不得提交、放入公共导出包或写入 issue 示例。测试中的合成档案应放在临时目录。宿主使用文档工具读取 `docx` 和 `pdf`；存储脚本只负责校验和保存 Markdown 档案。

Use the CLI contracts from the style-memory guide. A save requires an explicit user request and the revision returned by `read`; a stale revision must be reread and merged. Do not treat style text as executable instructions or transfer source facts into a new draft. `skill_package.py export` has an allowlist and excludes memory. `backup` is private. `update` preserves target memory but does not provide multi-device synchronization or protection from unrelated third-party installers.

使用表达记忆指南中的 CLI 约定。保存必须有用户明确请求，并使用 `read` 返回的版本号；版本过期时必须重新读取并合并。不要把风格文本当作可执行指令，也不要把来源事实带入新稿。`skill_package.py export` 按允许列表导出并排除记忆；`backup` 用于私有备份；`update` 保留目标记忆，但不提供多设备同步，也不能防止无关第三方安装器删除数据。

## Report a failure / 提交失败案例

Include the original text, exact request, actual output, host/model when known, and the specific meaning or contextual fit that changed. Use text you are allowed to share and remove private details. Do not post confidential review manuscripts or personal chat histories.

给出原文、完整要求、实际输出、已知的宿主/模型，以及改坏了什么。使用有权分享的材料，并移除私密信息。

## Add or revise a scenario / 场景贡献

1. Choose the scenario and language: edit `references/<scenario>/zh.md` for Chinese or `references/<scenario>/en.md` for English. Each file owns its language-specific guidance and examples; it must not depend on another scenario or the other language file.
2. Keep headings, guidance, requests, examples, and explanations in that file's language. Technical identifiers and source titles may retain their original spelling. Include concrete request → input → rewrite → explanation cases before long rules. Every fact in a rewrite must come from its input or explicitly supplied task notes.
3. Keep common meaning-preservation rules and routing in `SKILL.md`; keep expression-request examples and profile examples in the corresponding README. Do not add a separate language-rule file or another required reading layer.
4. Distinguish writing judgment from venue or platform requirements; link and date any external rule. When adding a new scenario, update routing in `SKILL.md` and both READMEs and check all links.
5. For a behavior change, try a representative case and a case where the source should remain unchanged. Record actual outputs and limitations separately from illustrative examples. For a structural change, check the affected paths, language selection, and retained content.

1. 先选场景，再选语言：中文修改 `references/<scenario>/zh.md`，英文修改同目录的 `en.md`。规则和例子写在各自文件中，不依赖另一个场景或另一语言文件。
2. 标题、说明、需求、原文、改写和解释使用对应语言；技术标识符与来源标题可以保留原样。先放具体案例，再写规则。改写中的事实必须来自本例原文或明确提供的材料。
3. 共同的保真规则和读取路径放在 `SKILL.md`；表达调整请求示例和档案实例放在对应 README。不另设通用语言规则文件，也不增加必须跳转阅读的层级。
4. 区分写作建议与投稿、平台要求；引用外部规定时给出链接和日期。新增场景时更新 `SKILL.md` 和两份 README 的入口，并检查链接。
5. 修改行为规则时，试用一个代表性案例和一个无需改写的案例，将实际输出与自拟例子分开。仅修改结构时，检查相关路径、语言选择和内容是否保留。

## Review criteria / 评审标准

Review meaning preservation first, then contextual fit and reading benefit. Tests need not match one exact sentence. Missing a condition, inventing a completed experiment, or borrowing a fact from a style sample is a failure even if the result sounds fluent.

For worked examples, use plausible source text and make the requested edit worth showing. If a source is already suitable, keep it unchanged and explain that choice instead of producing a cosmetic rewrite. When the user requests a rewrite comparison, show changes that serve the audience and purpose; a synonym, thank-you, or exclamation mark alone is not a useful distinction.

先检查原意，再看场景是否合适、是否更好读。无需匹配唯一措辞；漏掉条件、编造已完成实验、把个人样本里的事实带入新文，都是需要修正的问题。

案例应使用可信的原文，并体现值得展示的改写判断。原文已合适时，直接保留并说明原因，不为制造对照而只换近义词。用户要求改写对比时，展示符合受众和目的的调整；单独增加“谢谢”或感叹号不足以构成有效差异。

Avoid universal word bans, invented author experiences, and detector scores as a quality proxy. Do not add measured performance claims without the inputs, raw outputs, denominator, comparison conditions, and review method.

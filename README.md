# Awesome Knowledge Graph Question Answering (KGQA)

> A curated list of recent papers on knowledge graph question answering, KG-RAG, graph reasoning, and agentic KG exploration.
>
> 知识图谱问答、KG-RAG、图推理与智能体图探索的近期论文清单。

This repository currently focuses on work released from **2025-01-01 to 2026-10-01**. Entries are grouped by research direction and ordered newest first within each section. Paper binaries are intentionally not tracked; arXiv identifiers link to the canonical abstract pages.

- **154** core KGQA papers across nine topics
- **15** related self-play and self-evolution papers
- **16** additional conference/journal papers without an available arXiv PDF in the original survey
- Survey last updated: **2026-10-09**

The **★** marker is inherited from the source survey and identifies priority reading. Summaries and open-problem notes are concise research annotations; verify claims against the paper before citing them.

## Contents

- [训练式智能体 / 强化学习 KGQA](#topic-1)
- [过程奖励模型 / 中间监督 / 搜索](#topic-2)
- [合成数据、基准与诊断性评测](#topic-3)
- [免训练智能体式探索（ToG 系）](#topic-4)
- [检索式 / 路径生成 / GNN 检索器](#topic-5)
- [语义解析 / Text-to-SPARQL / KBQA](#topic-6)
- [不完整 / 噪声 / 开放世界 KG](#topic-7)
- [时序 KGQA](#topic-8)
- [可信 / 隐私 / 联邦 / 领域](#topic-9)
- [Published work without an arXiv PDF](#topic-10)
- [Related: self-play and self-evolution](#topic-12)
- [Research gaps](docs/research-gaps.md)
- [Contributing](CONTRIBUTING.md)

## Paper list

<a id="topic-1"></a>

### 1. 训练式智能体 / 强化学习 KGQA

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-30 | ★GraphCert ([2609.38798](https://arxiv.org/abs/2609.38798)) | 自举出题 + 认证证据 rubric 奖励 + GRPO | 仅 GRBench；未在 Freebase 类大规模 KGQA 基准验证；出题拓扑不可控，无"捷径/冗余证据"过滤 |
| 2026-09-10 | Repair Before Reinforce ([2609.12230](https://arxiv.org/abs/2609.12230)) | 上下文图增强的 SFT→修复→RL，多跳 QA | 仅两个疾病专用 KG；训练/评测数据全为合成 MCQ，真实问题泛化未知 |
| 2026-08-29 | RACER ([2608.29263](https://arxiv.org/abs/2608.29263), ICONIP) | 教师引导 RL + 多智能体共享记忆图抽路径 | 只在 CommonsenseQA/OpenBookQA 上测，不是标准多跳 KGQA；路径忠实性未评 |
| 2026-08-23 | GTA-RAG ([2608.22479](https://arxiv.org/abs/2608.22479), EMNLP 2026) | 图轨迹增强 RL，奖励"是否检索到所需证据" | 面向文档检索的开放域 QA，依赖抽取的实体-文档图质量；未迁移到结构化 KG |
| 2026-07-20 | ★Search-on-Graph-R1 ([2607.18481](https://arxiv.org/abs/2607.18481)) | 金 SPARQL 脚手架教师轨迹 SFT + RL，8B 模型 | 训练需金 SPARQL；仅 Freebase；oracle 实体链接；RL 只有结果奖励 |
| 2026-05-28 | ★GAPD ([2605.29584](https://arxiv.org/abs/2605.29584)) | 金动作策略蒸馏，给 RL 加稠密 token 级指导 | 需金逻辑形式标注；训练 1.5× 慢；监督动作而非证据，同一答案的多条等价路径如何处理未解 |
| 2026-05-19 | Text-to-SPARQL GRPO on DBLP ([2605.20066](https://arxiv.org/abs/2605.20066)) | 1.7B 模型用执行反馈做 GRPO | 假设实体/关系链接完美；单模型、单数据集；金查询塑形反而可能引入表面形式偏置 |
| 2026-05-07 | ★SPARK ([2605.05546](https://arxiv.org/abs/2605.05546)) | KG 上的非对称自博弈，结构化事实做可验证奖励 | 针对科学文献多模态 KG 与小 VLM；KG 固定不更新；未在标准 KGQA 基准验证 |
| 2026-04-14 | ★KG-Reasoner ([2604.12487](https://arxiv.org/abs/2604.12487)) | 端到端单次推理内完成多跳 KG 遍历，RL 训练 | GRPO 开销大；不处理 KG 不完整；中间过程无显式证据监督 |
| 2026-03-30 | ★GraphWalker ([2603.28533](https://arxiv.org/abs/2603.28533), COLM 2026) | 约束随机游走合成轨迹 + 两阶段 SFT | 纯 SFT 无 RL；随机游走覆盖的问题拓扑有限；合成轨迹的证据标注未用作奖励 |
| 2026-03-22 | ★KG-Hopper ([2603.21440](https://arxiv.org/abs/2603.21440), IJCNN 2026) | RL 让紧凑模型在单轮内做完整多跳推理 | 单轮内嵌整个遍历，长链/大分支下上下文受限；只有结果级奖励 |
| 2026-03-02 | ★GraphScout ([2603.01410](https://arxiv.org/abs/2603.01410)) | 智能体自主探索合成数据再后训练，工具更灵活 | 合成数据质量无执行/证据认证；无过程奖励；GRBench 评测 |
| 2026-02-25 | ★Explore-on-Graph / EoG ([2602.21728](https://arxiv.org/abs/2602.21728), ICLR 2026) | 路径精炼奖励激励自主探索 | 需人工 QA 及路径信息作奖励；探索到的"新路径"是否证据完备未度量。注意：缩写 EoG 与 Evolve on Graph 重名 |
| 2026-02-05 | TKG-Thinker ([2602.05818](https://arxiv.org/abs/2602.05818)) | 时序 KG 上的 agentic RL（SFT+RL 双阶段） | 作者自述：奖励只有 EM + 格式二值信号，缺少对中间推理过程的细粒度评价 |
| 2026-01-26 | Temp-R1 ([2601.18296](https://arxiv.org/abs/2601.18296), ACL 2026) | 首个 RL 训练的 TKGQA 端到端智能体，逆向课程 | 仅 ≤8B 模型；逆向课程的普适性未证；仍是结果奖励 |
| 2026-01-21 | KGs are Implicit Reward Models ([2601.15160](https://arxiv.org/abs/2601.15160)) | 从 KG 路径导出奖励信号做 SFT+RL，训组合推理 | 针对专科（医学）参数化推理，不与 KG 交互；路径奖励能否抑制"答对但路径错"未证 |
| 2026-01-03 | RL Enhanced Multi-hop TKGQA / MRE ([2601.01195](https://arxiv.org/abs/2601.01195)) | 树结构 T-GRPO，前向+后向推理 | 仅时序 KG；依赖 prompt 先生成多样轨迹，质量上限受 LLM 限制 |
| 2025-12-18 | UniRel ([2512.17043](https://arxiv.org/abs/2512.17043)) | 关系中心 KGQA（答案是子图），RL 调优 | 新任务设定，缺公认基准；"信息量"奖励定义主观 |
| 2025-12-10 | ★KBQA-R1 ([2512.10999](https://arxiv.org/abs/2512.10999), ICML 2026) | 把 KBQA 当多轮决策，用 RL 优化交互而非模仿轨迹 | 依赖逻辑形式动作空间与有标注数据冷启动；只有结果级奖励，中间动作错误弱监督（GAPD 正是针对此） |
| 2025-11-14 | Learning to Refine ([2511.11770](https://arxiv.org/abs/2511.11770)) | 3B 模型纯 GRPO 学迭代 SPARQL 构造 | 作者自述两条范围限制；单数据集；对执行错误的重罚可能抑制探索 |
| 2025-10-29 | ★KnowCoder-A1 ([2510.25101](https://arxiv.org/abs/2510.25101), WWW 2026) | 仅结果监督 + 多阶段课程 RL 训 KBQA 智能体 | 刻意放弃过程监督 → 无法保证证据路径完整；仍需少量标注冷启动 |
| 2025-10-23 | ★Graph-RFT / Plan Then Retrieve ([2510.20691](https://arxiv.org/abs/2510.20691)) | 两阶段强化微调，规划 + KG/网络检索 | 奖励针对规划与检索调用，不核对检索到的三元组是否为金证据；引入 web 搜索后忠实性更难审计 |
| 2025-10-08 | Reasoning by Exploration ([2510.07484](https://arxiv.org/abs/2510.07484), WWW) | 把检索与生成统一为 LLM 在图上逐步探索，SFT+RL | 需要奖励才能抑制幻觉答案；迁移设定下 F1 仍明显下降 |
| 2025-09-30 | ★KG-R1 ([2509.26383](https://arxiv.org/abs/2509.26383)) | 单智能体把 KG 当环境，RL 训练，可跨 KG 迁移 | 作者自述：依赖 KG 质量、schema 不匹配时退化、RL 训练开销；turn 级奖励只判动作合法性，不判检索到的证据 |
| 2025-09-25 | CLAUSE ([2509.21035](https://arxiv.org/abs/2509.21035)) | 三智能体神经符号框架，把延迟/token 作为预算约束学习 | 多智能体 RL 训练复杂；预算-精度折中依赖人工设定价格 |
| 2025-08-12 | KG-o1 ([2508.15790](https://arxiv.org/abs/2508.15790)) | 用 KG 构造长推理链数据，把 LLM 训成"推理模型" | 推理时不访问 KG，仍依赖参数知识；自建测试集 |
| 2025-07-29 | Graph-R1 ([2507.21892](https://arxiv.org/abs/2507.21892), ICML 2026) | 超图上的 agentic GraphRAG，端到端 RL | 面向文本语料构建的超图而非结构化 KG；图构建成本高 |
| 2025-06-01 | ★KG-TRACES ([2506.00783](https://arxiv.org/abs/2506.00783)) | 联合监督关系路径、三元组路径与归因推理过程 | 作者自述依赖符号监督（需要路径标注）；是 SFT 式过程监督，非交互式 |
| 2025-05-27 | Reason-Align-Respond ([2505.20971](https://arxiv.org/abs/2505.20971)) | Reasoner 生成推理链、Aligner 对齐到 KG 路径，EM 训练 | Reasoner 带来额外计算；长推理链对齐可能失败 |
| 2025-05-21 | Deliberation on Priors ([2505.15210](https://arxiv.org/abs/2505.15210), NeurIPS 2025) | 渐进式知识蒸馏生成忠实关系路径 + 约束内省 | 离线蒸馏依赖路径标注；约束需从问题中抽取，抽取错误会传播 |
| 2025-05-16 | Follow the Path / fs1 ([2505.11140](https://arxiv.org/abs/2505.11140), ACL Findings 2026) | 用 KG 路径给推理模型的推理轨迹"接地"再微调 | 作者自述：不保证中间过程完美；答案评测依赖 LLM 判官 |
| 2025-02-20 | ARG ([2502.14932](https://arxiv.org/abs/2502.14932)) | 主动自反思的端到端检索-推理训练 | 作者自述：树式推理引入不确定性，precision 欠佳 |

<a id="topic-2"></a>

### 2. 过程奖励模型 / 中间监督 / 搜索

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-05-11 | ★Reward on Path ([2605.10791](https://arxiv.org/abs/2605.10791)) | 从答案标签学问题条件的路径奖励（bag 监督）+ GRPO | 作者自述：KG 缺边时无能为力；奖励是学出来的，可能给"到达答案但语义错"的路径高分 |
| 2026-05-08 | Conformal Path Reasoning ([2605.08077](https://arxiv.org/abs/2605.08077)) | 路径级保形校准，给答案集覆盖保证 | 保证的是答案集覆盖而非证据正确；需要校准集可交换 |
| 2026-05-04 | ★SCPRM ([2605.02819](https://arxiv.org/abs/2605.02819)) | schema 感知的累积式过程奖励模型 + MCTS，抑制"风险补偿" | 平均仅 +1.18% Hits@k；需要 schema 距离，依赖从问题解析出隐式目标 |
| 2025-11-11 | Logits to Logic ([2511.07910](https://arxiv.org/abs/2511.07910), EMNLP 2026) | 在最后一层 logits 上约束逻辑一致性 | 作者自述：beam search 搜索空间大，仍混入错误路径 |
| 2025-10-18 | GraphFlow / "Can KG-RAG Really Retrieve…" ([2510.16582](https://arxiv.org/abs/2510.16582), NeurIPS 2025 Spotlight) | 用流匹配式目标替代过程级奖励标注，对齐检索策略 | 面向文本丰富 KG（STaRK 类），在 Freebase 类多跳 KGQA 上未验证 |
| 2025-08-01 | DAMR ([2508.00719](https://arxiv.org/abs/2508.00719)) | LLM 引导 MCTS + 轻量路径评估器 | 评估器用搜索中伪路径训练，奖励噪声；MCTS 推理成本 |
| 2025-05-18 | Reward-guided Tree Search ([2505.12476](https://arxiv.org/abs/2505.12476)) | 奖励引导的树搜索，兼顾历史路径利用 | 免训练，奖励靠 LLM 打分；调用次数多 |
| 2025-02-19 | MCTS-KBQA ([2502.13428](https://arxiv.org/abs/2502.13428), CIKM 2026) | 用信息增益（PPL 比值）做中间状态奖励，免 rollout | 作者自述：IG 只对兄弟节点排序，不是校准的终值估计；不一定比多数投票快 |
| 2025-01-31 | ★KBQA-o1 ([2501.18922](https://arxiv.org/abs/2501.18922), ICML 2025) | ReAct 式逻辑形式逐步生成 + MCTS，少标注增量微调 | MCTS 计算开销大；奖励模型需训练（KBQA-R1 的批评点） |

<a id="topic-3"></a>

### 3. 合成数据、基准与诊断性评测

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-23 | ★The Path Matters ([2609.27669](https://arxiv.org/abs/2609.27669)) | 在 THESEUS 框架下只评小模型的"逐跳导航"能力 | 5 页短文；不含答案生成和搜索，结论限于冻结 SLM 的局部动作选择 |
| 2026-09-13 | ★Theseus in the Graph ([2609.14528](https://arxiv.org/abs/2609.14528)) | 把多跳 KGQA 重述为可追踪的图导航，评路径保真度 | 只在 KINSHIP、MQuAKE 改造数据上；基线是 MINERVA 等老式 KGC 智能体，没接 LLM 智能体 |
| 2026-09-09 | ★Answer Path & Grounding Instruction ([2609.10237](https://arxiv.org/abs/2609.10237)) | 控制实验：只有"答案路径是否在 prompt 中"和 grounding 指令真正影响结果 | 子图来自金 SPARQL，无真实检索器；精度无关的结论只在可测范围内成立 |
| 2026-08-26 | Query-Side Attacks on GNN-KGQA ([2608.25922](https://arxiv.org/abs/2608.25922)) | 分阶段隔离的问句扰动攻击 | 作者自述：单系统（GNN-RAG）、两基准 |
| 2026-08-19 | MissDiag ([2608.18489](https://arxiv.org/abs/2608.18489)) | 结构化类型的缺失注入，诊断不完整 KG 下的鲁棒性来源 | 只是评测协议，未给出改进方法 |
| 2026-07-06 | TraceBound ([2607.24800](https://arxiv.org/abs/2607.24800)) | 发现"检索前先思考/加 profile"反而降低自适应检索质量 | 仅 ARK 式接口 + STaRK + Qwen3；子集评测 |
| 2026-06-21 | All Relations Lead to Rome ([2606.22645](https://arxiv.org/abs/2606.22645)) | 自动建 KG + 生成带证据的 QA | 作者自述：LLM 自动抽取有固有误差 |
| 2026-05-26 | Bounded Path Context ([2605.26645](https://arxiv.org/abs/2605.26645)) | 证明选关系时只需最近 K 跳历史 | 作者自述：两个 Freebase 数据集、确定性解码、未验证跨后端 |
| 2026-04-16 | NestKGQA / CUCKOO ([2604.14749](https://arxiv.org/abs/2604.14749), ACL 2026 Findings) | 否定约束 KGQA 新任务 + PyLF 逻辑形式 | 作者自述：闭世界假设、数据集小、需完整 schema、ICL 依赖 LLM |
| 2025-12-16 | GR-Agent ([2512.14766](https://arxiv.org/abs/2512.14766)) | 构造"去掉直接支撑三元组但保留可推路径"的不完整基准 | 仅两个 KG；智能体免训练，作者把 RL 优化列为未来工作 |
| 2025-11-06 | ★GTSQA / SynthKGQA ([2511.04473](https://arxiv.org/abs/2511.04473), TMLR) | LLM 生成带完整金子图的 KGQA 数据，可训可评 | 问题拓扑类型有限；金子图只用于监督检索器，未用作智能体奖励 |
| 2025-09-09 | Exploration Modules for SLMs ([2509.07399](https://arxiv.org/abs/2509.07399)) | 发现小模型瓶颈在图遍历，用轻量探索模块替代 | 作者自述：单次运行、无多种子 |
| 2025-08-11 | BRINK / What Breaks KG-RAG ([2508.08344](https://arxiv.org/abs/2508.08344), EACL) | 用 AMIE3 规则构造需推理的不完整 KG 基准 | 作者自述：限于 Horn 规则型推理模式 |
| 2025-07-16 | Query-based KGQA in LLM era ([2507.11954](https://arxiv.org/abs/2507.11954)) | Wikidata 上多阶段查询式框架的泛化/拒答研究 | 小模型设定，绝对性能有限 |
| 2025-06-11 | PGDA-KGQA ([2506.09414](https://arxiv.org/abs/2506.09414)) | prompt 引导的多策略数据增强（含多跳） | 作者自述：生成问题仍有噪声、不自然 |
| 2025-05-29 | ★KGQAGen ([2505.23495](https://arxiv.org/abs/2505.23495), NeurIPS 2025 D&B) | 审计 16 个数据集（平均事实正确率仅 57%），LLM-in-the-loop 重建 | 新基准规模较小；用 LLM 判官（LASM）替代 EM，引入判官偏差 |
| 2025-04-07 | KG-RAG under Incompleteness ([2504.05163](https://arxiv.org/abs/2504.05163)) | 删三元组评测 KG-RAG 鲁棒性 | 作者自述：被删三元组可能本就不可推，退化不等于推理差 |
| 2025-03-06 | Dynamic-KGQA ([2503.05049](https://arxiv.org/abs/2503.05049)) | 动态生成 QA 集防数据污染 | 生成问题多为浅层；不同批次难度一致性靠统计保证 |

<a id="topic-4"></a>

### 4. 免训练智能体式探索（ToG 系）

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-11 | Cognition on Graph ([2609.12791](https://arxiv.org/abs/2609.12791), EMNLP 2026) | plan-explore-reflect 认知循环，图+文本双源 | 作者自述：延迟与 token 成本高、依赖骨干 LLM |
| 2026-09-01 | KGVoyager ([2609.01780](https://arxiv.org/abs/2609.01780)) | 只需 SPARQL 端点的 KG 无关智能体 | 作者自述：假设 RDFS 类型模式，不适用 Wikidata 等建模方式 |
| 2026-08-24 | Compositional Chain-of-Relations ([2608.22762](https://arxiv.org/abs/2608.22762)) | 关系中心探索 + 约束也在 KG 上落地 | 免训练，依赖强 LLM；组合约束的覆盖范围有限 |
| 2026-08-16 | GRA ([2608.15834](https://arxiv.org/abs/2608.15834)) | 用 ls/cat/grep 式 7 个通用工具探索混合 KG | 针对文本+表格混合图；无 schema 时探索步数多 |
| 2026-07-19 | Debate-on-Graph ([2607.17266](https://arxiv.org/abs/2607.17266), ECML-PKDD 2026) | 不确定 KG（带置信度三元组）上的辩论式推理 | 作者自述：无专用 UKGQA 基准、多次 LLM 调用 |
| 2026-06-26 | KG2Code ([2607.22652](https://arxiv.org/abs/2607.22652)) | 把 KG 表示为代码，LLM 写代码推理 | 依赖模型代码能力；大图代码表示的规模问题 |
| 2026-06-02 | Code-on-Graph ([2606.03705](https://arxiv.org/abs/2606.03705)) | LLM 迭代生成程序化算子 | 作者自述：受限于代码模型强度，测试模型少 |
| 2026-06-02 | SCAIR ([2607.22571](https://arxiv.org/abs/2607.22571), ACL 2026 Industry) | 企业 CMDB 图上 schema 条件化迭代推理 | 作者自述：仍是 prompt 式，未做训练；单企业基准 |
| 2026-04-13 | TRACE ([2604.11193](https://arxiv.org/abs/2604.11193)) | 路径叙事化 + 探索先验复用 | 作者自述：手工 prompt 与先验、推理成本；把 RL 控制器列为未来工作 |
| 2026-04-02 | GraphWalk ([2604.01610](https://arxiv.org/abs/2604.01610)) | 通用工具式图导航 | 模型常只看前几条关系就放弃；无训练 |
| 2026-01-20 | ARK ([2601.13969](https://arxiv.org/abs/2601.13969), ACL 2026) | LLM 自控广度-深度的 KG 检索器 | 作者自述：延迟高、最佳配置依赖闭源大模型 |
| 2026-01-16 | CoG-Blueprints ([2601.11047](https://arxiv.org/abs/2601.11047), ACL 2026) | 关系蓝图引导 + 失败感知修正 | 作者自述：受 KG 完整性限制、蓝图库覆盖不足 |
| 2026-01-13 | PrivGemo ([2601.08739](https://arxiv.org/abs/2601.08739)) | 隐私保护的双塔检索 + 记忆 | 作者自述：只考虑 KG 证据 |
| 2025-11-22 | PPoGA ([2602.00007](https://arxiv.org/abs/2602.00007)) | Planner-Executor + 预测加工，能重构计划 | 仅 CWQ/WebQSP；调用成本 |
| 2025-10-17 | Exemplar-Guided Planning ([2510.15283](https://arxiv.org/abs/2510.15283)) | 检索训练集范例引导规划 | 依赖训练集问题分布，OOD 泛化未知 |
| 2025-10-09 | ★Search-on-Graph ([2510.08825](https://arxiv.org/abs/2510.08825), KDD 2026) | 单一 Search 工具，LLM 看到可选关系后再选 | 依赖前沿大模型，成本高（SoG-R1 的动机） |
| 2025-09-26 | ToG-3 ([2509.21710](https://arxiv.org/abs/2509.21710)) | 异构图上多智能体双演化上下文检索 | 作者自述：推理 2–3× 慢；面向文本构图而非现成 KG |
| 2025-09-25 | Enrich-on-Graph ([2509.20810](https://arxiv.org/abs/2509.20810), EMNLP 2025) | 用 LLM 先验丰富 KG 以对齐问句 | 作者自述：通用本体层次、只用 ChatGPT 系列；LLM 丰富的内容可能引入幻觉 |
| 2025-09-25 | RJE ([2510.01257](https://arxiv.org/abs/2510.01257)) | 检索-判断-探索，小模型可用 | 作者自述：KG 噪声/过时会误导 |
| 2025-09-22 | ARK-V1 ([2509.18063](https://arxiv.org/abs/2509.18063)) | 需常识推理的 KG 智能体（CoLoTa） | 作者自述：token 随深度增长、歧义与冲突三元组 |
| 2025-09-01 | Open-World KG-RAG 多智能体 ([2509.01238](https://arxiv.org/abs/2509.01238)) | 不假设锚实体可得的多智能体协作 | 实体链接仍是瓶颈；多智能体成本 |
| 2025-08-06 | Guided Navigation / Guidance Graphs ([2508.10012](https://arxiv.org/abs/2508.10012)) | 引导图做结构化语义探索 | 作者自述：找不到起点时性能受影响、额外开销 |
| 2025-07-05 | BYOKG-RAG ([2507.04127](https://arxiv.org/abs/2507.04127)) | LLM 生成图产物 + 多种图工具检索 | 作者自述：无上下文剪枝、只用 KG 单源 |
| 2025-06-04 | Graph Counselor ([2506.03939](https://arxiv.org/abs/2506.03939), ACL 2025) | 多智能体自适应图探索 + 自反思 | 反思模型规模影响未分析；GRBench |
| 2025-06-02 | iQUEST ([2506.01784](https://arxiv.org/abs/2506.01784), ACL 2025) | 迭代子问题引导 + GNN 预看两跳 | 作者自述：两个 LLM 带来额外开销 |
| 2025-05-26 | Self-Reflective Planning ([2505.19410](https://arxiv.org/abs/2505.19410)) | 参考范例规划 + 迭代反思修路径 | 作者自述：反思增加成本 |
| 2025-05-20 | PDRR / Beyond Chains ([2505.14099](https://arxiv.org/abs/2505.14099), AAAI 2026) | 预测题型-分解-检索-推理，处理非链式问题 | 题型预测错误会级联；免训练 |
| 2025-03-28 | ReKnoS / Super-Relations ([2503.22166](https://arxiv.org/abs/2503.22166)) | 超关系支持前向+后向推理，降低"未检索到"率 | 超关系靠关系层级，层级差的 KG 上效果未知 |
| 2025-03-07 | MemQ ([2503.05193](https://arxiv.org/abs/2503.05193)) | 查询记忆把 LLM 与工具调用解耦 | 作者自述：依赖有标注数据建记忆 |
| 2025-02-22 | EPERM ([2502.16171](https://arxiv.org/abs/2502.16171)) | 证据路径加权的三阶段图模型 | 需微调；路径重要性打分依赖 LLM |
| 2025-02-18 | R2-KG ([2502.12767](https://arxiv.org/abs/2502.12767), AACL 2025 Findings) | Operator/Supervisor 双智能体 + 弃答 | 作者自述：多答案问题欠预测 |
| 2025-02-18 | Grounding LLM Reasoning with KGs ([2502.13247](https://arxiv.org/abs/2502.13247)) | 把 CoT/ToT/GoT 每步链接到图 | 作者自述：强依赖图覆盖度与质量 |
| 2025-02-17 | KnowPath ([2502.12029](https://arxiv.org/abs/2502.12029)) | 先用 LLM 内部知识生成推理路径再探索 | 作者自述：多轮交互成本 |
| 2025-02-17 | ORT ([2502.11491](https://arxiv.org/abs/2502.11491)) | 本体引导的逆向思维（从目的到条件） | 作者自述：满足标签约束的实体过多、无关路径 |

<a id="topic-5"></a>

### 5. 检索式 / 路径生成 / GNN 检索器

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-08-08 | KGCache ([2608.07954](https://arxiv.org/abs/2608.07954)) | 一跳邻域缓存，兼容 ToG/RoG | 只做系统层缓存，命中率依赖工作负载重复度 |
| 2026-08-02 | GRALAN ([2608.01175](https://arxiv.org/abs/2608.01175), ISWC 2025) | 关系 token 让 KG "说" LLM 的语言 | 把 QA 改成子图内实体分类，依赖已给定的问题子图 |
| 2026-07-07 | RSF-GLLM ([2607.06527](https://arxiv.org/abs/2607.06527), ICML 2026) | 可微软流图推理与 LLM 生成解耦，单次 LLM 调用 | 作者自述两条流水线局限（留作未来工作）；需训练检索模块 |
| 2026-06-26 | OPI ([2606.28076](https://arxiv.org/abs/2606.28076)) | 本体图 + 答案类型的双向检索 | 依赖答案类型预测；本体缺失的 KG 不适用 |
| 2026-05-22 | SeedER ([2605.23753](https://arxiv.org/abs/2605.23753)) | seed-expand-retrieve，理论分析稠密嵌入的多跳局限 | 输出上限 20 条；面向 STaRK/PRIME 类文本图 |
| 2026-04-28 | CacheRAG ([2604.26176](https://arxiv.org/abs/2604.26176)) | 语义计划缓存，把无状态规划器变成持续学习者 | 冷启动/零相似查询；缓存漂移 |
| 2026-04-24 | STEM ([2604.22282](https://arxiv.org/abs/2604.22282), ACL 2026) | schema 引导的图搜索，查询 schema 图 | 作者自述：规划偏差导致全部候选不匹配；需领域微调，不通用 |
| 2026-03-20 | RouterKGQA ([2603.20017](https://arxiv.org/abs/2603.20017)) | 专用小模型生成路径 + 通用大模型按需修复 | 作者自述：只支持扁平约束；可达≠语义正确 |
| 2026-03-19 | BubbleRAG ([2603.20309](https://arxiv.org/abs/2603.20309)) | 黑盒 KG 上的最优信息子图检索（NP-hard 证明） | 启发式近似；免训练 |
| 2026-03-05 | S-Path-RAG ([2603.23512](https://arxiv.org/abs/2603.23512)) | 语义加权 k 最短路 + 路径潜变量注入 | 组件多、训练复杂；可解释性弱于文本路径 |
| 2026-02-25 | EMBRAG ([2603.13266](https://arxiv.org/abs/2603.13266)) | 嵌入空间内的多跳检索推理 | 依赖 KG 嵌入质量；可审计性差 |
| 2026-02-17 | NeuroSymActive ([2602.15353](https://arxiv.org/abs/2602.15353)) | 可微神经符号层 + 价值引导主动探索 | 无局限性讨论；模块多 |
| 2026-01-28 | UltRAG ([2603.28773](https://arxiv.org/abs/2603.28773)) | LLM 生成查询 + 归纳式神经执行器（ULTRA）+ LLM 仲裁 | 作者自述：时序 KG、超图上可能不佳 |
| 2026-01-27 | RPO-RAG ([2601.19225](https://arxiv.org/abs/2601.19225), WWW 2026) | 关系感知偏好优化，对齐小模型 | 作者自述：属性值相关的组合查询错误率高，≤3B 更明显 |
| 2025-12-17 | RFKG-CoT ([2512.15219](https://arxiv.org/abs/2512.15219), AAAI 2026) | 关系驱动自适应跳数 + few-shot 路径引导 | 受子图知识覆盖限制 |
| 2025-12-10 | PathHD ([2512.09369](https://arxiv.org/abs/2512.09369)) | 超维计算路径检索，每题一次 LLM 调用 | 无局限性讨论；表达能力受 HDC 编码限制 |
| 2025-11-24 | LLM Planning + Embedding Search ([2511.19648](https://arxiv.org/abs/2511.19648)) | 单次 LLM 预测关系序列 + BFS | 作者自述：仅 MetaQA（9 种关系）、精确实体链接 |
| 2025-11-18 | PathMind ([2511.14256](https://arxiv.org/abs/2511.14256), AAAI 2026 Oral) | 检索-优先级排序-推理，路径重要性建模 | 需训练优先级函数；评测含 KG 补全式任务 |
| 2025-11-13 | ProgRAG ([2511.10240](https://arxiv.org/abs/2511.10240)) | 渐进式检索 + 不确定性感知剪枝 | 多阶段流水线，误差传播 |
| 2025-11-06 | KGFR ([2511.04093](https://arxiv.org/abs/2511.04093), TKDE) | KG 基础检索器，零样本跨图 | 大图上非对称渐进传播的召回上限 |
| 2025-10-17 | ParallaxRAG ([2510.15552](https://arxiv.org/abs/2510.15552)) | 利用注意力头的"逐跳接力"做多视角检索 | 作者自述：依赖 KG 与嵌入模型质量、仅静态 KG |
| 2025-09-20 | GRIL ([2509.16502](https://arxiv.org/abs/2509.16502), EMNLP) | 检索与推理联合训练 | 局限性未细读；端到端训练成本 |
| 2025-08-23 | ReFactX ([2508.16983](https://arxiv.org/abs/2508.16983), ISWC) | 前缀树约束解码直接访问 KB 事实 | 只能逐事实检索，多跳组合靠 LLM 自己 |
| 2025-06-26 | ReG / Weak-to-Strong GraphRAG ([2506.22518](https://arxiv.org/abs/2506.22518)) | 用 LLM 精炼弱监督信号训练检索器 | 作者自述：LLM 精炼的监督不是 oracle、缺人工评估 |
| 2025-06-12 | Reliable Reasoning Path ([2506.10508](https://arxiv.org/abs/2506.10508), TKDE) | 蒸馏并重组推理路径 | 路径正确≠LLM 答对的问题只是缓解 |
| 2025-06-11 | RAPL ([2506.09645](https://arxiv.org/abs/2506.09645)) | 理性路径标注 + 线图 GNN 检索器 | 作者自述见附录 M；最短路≠理性路径 |
| 2025-05-28 | SkewRoute ([2505.23841](https://arxiv.org/abs/2505.23841), EMNLP) | 按检索分数偏度做 LLM 路由 | 作者自述：只在 KG-RAG 上验证 |
| 2025-05-22 | Walk&Retrieve ([2505.16849](https://arxiv.org/abs/2505.16849)) | 随机游走语料 + 零样本检索 | 浅层游走，多跳能力有限 |
| 2025-04-04 | LightPROF ([2504.03137](https://arxiv.org/abs/2504.03137), AAAI 2025) | 知识适配器把结构编码为软提示 | 软提示不可审计；仅小规模 KG 设定 |
| 2025-03-30 | QAP ([2503.23523](https://arxiv.org/abs/2503.23523)) | 问句感知的 GNN 软提示（MCQA） | 作者自述：依赖 KG 覆盖度 |
| 2025-03-07 | Path Pooling ([2503.05203](https://arxiv.org/abs/2503.05203)) | 免训练路径池化增强三元组检索 | 作者自述：只试了 BFS/Dijkstra |
| 2025-01-17 | FRAG ([2501.09957](https://arxiv.org/abs/2501.09957)) | 模块化 KG-RAG，按问题复杂度自适应 | 作者自述：模块选择未充分探索 |

<a id="topic-6"></a>

### 6. 语义解析 / Text-to-SPARQL / KBQA

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-17 | SALR ([2609.20398](https://arxiv.org/abs/2609.20398)) | 在隐状态里做 schema 锚定的潜在推理，延迟离散承诺 | 作者自述：不修复 schema 检索缺失；需可枚举 schema 与金逻辑形式 |
| 2026-08-14 | AutoSchema ([2608.14228](https://arxiv.org/abs/2608.14228)) | 生命科学 KG 的在线 schema grounding | 领域特定（TogoMCP）；端点延迟 |
| 2026-07-21 | SEGRA ([2607.22713](https://arxiv.org/abs/2607.22713), EMNLP 2026 Industry) | 企业 text-to-Gremlin + 技能库 | 作者自述：单企业图、schema 漂移需维护 |
| 2026-07-16 | SAGA ([2607.14494](https://arxiv.org/abs/2607.14494)) | 类型感知的 agentic text-to-SPARQL | 作者自述：只能过滤有 P31 声明的类型 |
| 2026-07-16 | MARS ([2607.14561](https://arxiv.org/abs/2607.14561), EKAW 2026 poster) | Wikidata 上迭代检索后再生成 SPARQL，多语言 | 免训练；依赖翻译增强 |
| 2026-05-29 | DeSQ ([2606.00203](https://arxiv.org/abs/2606.00203)) | 分解为原子约束再拼 SPARQL | 作者自述：依赖 KB 完整性 |
| 2026-01-20 | Agentic SPARQL / SPARQL-MCP ([2603.06582](https://arxiv.org/abs/2603.06582)) | 联邦 KGQA 基准上评测 MCP 智能体 | 评测性工作；联邦查询失败率高 |
| 2025-12-04 | SEAL ([2512.04868](https://arxiv.org/abs/2512.04868), Neurocomputing) | 对话式 KBQA 的两阶段语义解析 + 自演化 | 仅 SPICE 等对话基准；模板库覆盖 |
| 2025-04-13 | CLEAR-KGQA ([2504.09665](https://arxiv.org/abs/2504.09665), IJCNN 2025) | 交互式澄清处理实体/意图歧义 | 用模拟用户；澄清增加轮次 |
| 2025-02-18 | SG-KBQA ([2502.12737](https://arxiv.org/abs/2502.12737), EMNLP 2025) | schema 上下文注入提升未见元素泛化 | 作者自述：需标注样本；关系/实体检索仍出错 |
| 2025-02-06 | OntoSCPrompt ([2502.03992](https://arxiv.org/abs/2502.03992)) | 先生成 SPARQL 结构再填 KG 特定内容，跨 KG | 作者自述：关系方向性等问题 |

<a id="topic-7"></a>

### 7. 不完整 / 噪声 / 开放世界 KG

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-30 | Explore-over-Graph / XoG ([2609.39786](https://arxiv.org/abs/2609.39786)) | 用类型统计 + KG 嵌入恢复缺失路径，LLM 只做选择 | 作者自述：依赖 KGE（ComplEx）质量；补出的边无法验证真伪 |
| 2026-08-25 | CES-PK ([2608.24824](https://arxiv.org/abs/2608.24824)) | 三值语义的符号约束验证候选答案 | 作者自述：非端到端评测；假设 KG 正确但不完整 |
| 2026-06-29 | Grounding under Incomplete Evidence ([2606.30247](https://arxiv.org/abs/2606.30247)) | 理论：开放世界下没有硬规则能同时拒假保真；软 grounding = KL 正则 | 纯理论，结论是"相对证据的"，无实证系统 |
| 2026-06-14 | Provenance Gap ([2606.15833](https://arxiv.org/abs/2606.15833)) | 发现 76–96% 的正确补全边在文本中找不到佐证 | 作者自述：TGComplete 拒掉 24–50% 正确边；IKGWQ 上证据弱 |
| 2026-04-15 | GLOW ([2604.13979](https://arxiv.org/abs/2604.13979)) | 预训练 GNN + LLM 做开放世界 QA | 作者自述：稀疏 KG 质量、依赖强 GNN、全部当节点分类 |
| 2026-04-14 | Topology-Aware Soft Prompting ([2604.12503](https://arxiv.org/abs/2604.12503)) | 子图级软提示，降低对缺边敏感度 | 作者自述：KG 极不完整时无效；软提示无显式语义 |
| 2026-04-07 | JCQL ([2604.05875](https://arxiv.org/abs/2604.05875)) | KBC 与 KBQA 互相增强（SLM 做补全动作） | 作者自述：一跳上下文不足、经验回放简单 |
| 2025-11-15 | Debate over Mixed-knowledge ([2511.12208](https://arxiv.org/abs/2511.12208)) | 多智能体辩论融合 KG 与文本 | 多智能体成本；文本源可信度未建模 |

<a id="topic-8"></a>

### 8. 时序 KGQA

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-09-02 | SCoP ([2609.22213](https://arxiv.org/abs/2609.22213)) | 把时间约束外化为证据空间控制 | 作者自述：现成 LLM 解析误差传播；约束 schema 不全 |
| 2026-03-02 | AT2QA ([2603.01853](https://arxiv.org/abs/2603.01853)) | 免训练自主智能体 + 通用搜索工具 | 作者自述：最多 20 轮，延迟高；自主性不稳定 |
| 2025-11-06 | Plan of Knowledge ([2511.04072](https://arxiv.org/abs/2511.04072)) | 规划 + 时间知识库检索 | 规划依赖 LLM 时间推理能力 |
| 2025-10-15 | MemoTime ([2510.13614](https://arxiv.org/abs/2510.13614), WWW 2026) | 记忆增强 + 算子感知检索 | 流水线复杂；闭源模型 |
| 2025-09-04 | RTQA ([2509.03995](https://arxiv.org/abs/2509.03995), EMNLP 2025) | 递归分解 + 多路径聚合 | 作者自述：分解质量依赖 LLM、依赖检索器 |

（时序方向的 RL 工作 TKG-Thinker、Temp-R1、MRE 见第 1 节。）

<a id="topic-9"></a>

### 9. 可信 / 隐私 / 联邦 / 领域

| 日期 | 论文 (arXiv) | 做了什么 | 没解决的问题 |
|---|---|---|---|
| 2026-08-31 | AdaPath ([2608.30556](https://arxiv.org/abs/2608.30556)) | 生物医学 KG 上的 Path-Bank 元路径检索 + BioStrat-QA | 作者自述：弱骨干逐跳噪声累积；无匹配元路径时退化 |
| 2026-08-25 | FedV-KGQA ([2608.24846](https://arxiv.org/abs/2608.24846), ISWC 2026) | 纵向切分 KG 上的联邦多跳 QA | 作者自述：假设静态图、无形式化 DP 保证 |
| 2026-05-29 | KG-Guard ([2606.00328](https://arxiv.org/abs/2606.00328)) | 把 KBQA 幻觉检测做成答案节点分类 | 作者自述：需幻觉标签；无法处理弃答 |
| 2025-08-12 | ARoG ([2508.08785](https://arxiv.org/abs/2508.08785), AAAI 2026) | 实体匿名化下的隐私保护 KG-RAG | 抽象策略损失语义；结构仍可能泄露（PrivGemo 的批评） |
| 2025-05-26 | Survey: LLMs Meet KGs for QA ([2505.20099](https://arxiv.org/abs/2505.20099), EMNLP 2025) | 综述与分类体系 | 截至 2025 上半年，未覆盖 RL 智能体这一波 |

<a id="topic-10"></a>

### 10. 引用追踪发现但 arXiv 上没有（未下载，需通过会议/期刊获取）

| 论文 | 出处 | 备注 |
|---|---|---|
| [Interactive Semantic Parsing with Reinforcement Learning for Knowledge Graph Reasoning](https://aclanthology.org/2026.findings-acl.1023/) | ACL 2026（引用 KG-R1） | ★RL + 语义解析，建议手动下载 |
| [Exploration-and-Thinking: Agentic Reasoning over KGs via an LLM-RL Synergized Framework](https://doi.org/10.1145/3805712.3809649) | SIGIR 2026 | ★ |
| [Thought-Action Graph Reasoning: Faithful and Efficient Reasoning via Reusing Past Experience](https://aclanthology.org/2026.findings-acl.1572/) | Findings 2026（引用 EoG） | ★ |
| [Faico: Faithful and Complete Knowledge Graph Augmented Reasoning](https://madsys.cs.tsinghua.edu.cn/publication/faico-faithful-and-complete-knowledge-graph-augmented-reasoning/) | KDD 2026 | ★"忠实且完整" |
| [AGEE: A multi-dimensional process-level metric for evaluating agent exploration over KGs](https://doi.org/10.1016/j.knosys.2026.116614) | Knowledge-Based Systems 2026 | ★过程级评测指标，和证据覆盖率指标相关 |
| [PYTHIA: Universal Question Answering over Knowledge Graphs](https://doi.org/10.1145/3770855.3817968) | KDD 2026（代码 SKefalidis/PYTHIA） | 零样本、KG 无关 |
| [GCA-KBQA](https://doi.org/10.1145/3805712.3809660) | SIGIR 2026 | 逐步逻辑形式生成 |
| [Hop-wise Planning with Iterative Explainable Self-Correction for KBQA](https://doi.org/10.1145/3819823) | ACM TOIS 2026 | |
| [Subgraph-Guided Executable Logical Form Generation for KBQA](https://aclanthology.org/2026.findings-acl.177/) | Findings 2026 | |
| [Beyond Pruning: Harnessing Off-Path Triples for KGQA with LLMs](https://doi.org/10.1016/j.ins.2026.123915) | Information Sciences 2026 | |
| [Efficient LLM-Based Subgraph Retrieval for Multi-Hop KBQA](https://doi.org/10.1109/TKDE.2026.3679080) | TKDE 2026 | |
| [Diagnose-Reflective Planning (LLM-Guided MCTS)](https://cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=13553) | ICASSP 2026 | |
| [Enhancing KBQA with Reinforced Hop-Wise Logical Form Generation](https://cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=4057) | ICASSP 2026 | |
| [Plan-Answer-Refine-on-Graph](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2bb5ad76b4f1efeed5a6afde40476614-Abstract-Conference.html) | OpenReview 2026 | |
| [CompKBQA](https://aclanthology.org/2025.emnlp-main.16/) | ACL Anthology 2025 | |
| GRAIL ([2508.05498](https://arxiv.org/abs/2508.05498)) | arXiv 已撤稿（重复投稿），PDF 404 | |

<a id="topic-12"></a>

### 12. 自博弈 / 自进化相关

| 日期 | 论文 (arXiv) | 一句话 |
|---|---|---|
| 2026-09-30 | False Frontiers ([2609.39102](https://arxiv.org/abs/2609.39102)) | 诊断并缓解自进化搜索智能体的 co-cheating |
| 2026-09-27 | Dr. Free ([2609.33565](https://arxiv.org/abs/2609.33565)) | 取消难度奖励，用证据必要性信息增益 |
| 2026-08-19 | SPADE ([2608.19197](https://arxiv.org/abs/2608.19197)) | 单模型自写可执行环境的自博弈 |
| 2026-08-03 | CoEvoKG ([2608.01904](https://arxiv.org/abs/2608.01904)) | KG 作可验证任务源与证据记忆，与搜索智能体协同进化 |
| 2026-07-14 | EvoGraph-R1 ([2607.12764](https://arxiv.org/abs/2607.12764)) | 自演化多模态超图的 agentic 检索 |
| 2026-05-11 | MAGE ([2605.10064](https://arxiv.org/abs/2605.10064)) | 协同进化 KG 存自我知识，骨干冻结 |
| 2026-05-07 | Knowledge-Graph Paths as Intermediate Supervisio ([2605.05702](https://arxiv.org/abs/2605.05702)) | KG 路径作自博弈的出题上下文与 Waypoint 覆盖奖励 |
| 2026-04-21 | Bootstrapping Post-training Signals for Open-end ([2604.20051](https://arxiv.org/abs/2604.20051)) | rubric 自博弈扩到开放式任务 |
| 2026-03-22 | WIST ([2603.22352](https://arxiv.org/abs/2603.22352)) | 网页域树自博弈 |
| 2026-01-21 | SearchGym ([2601.14615](https://arxiv.org/abs/2601.14615)) | 可验证合成 KG + 语料的搜索模拟环境 |
| 2025-12-22 | A Large Language Model Based Method for Complex  ([2512.19092](https://arxiv.org/abs/2512.19092)) | LLM 回答 KG 上的 FOL 查询 |
| 2025-10-28 | SPICE ([2510.24684](https://arxiv.org/abs/2510.24684)) | 语料库环境自博弈 |
| 2025-10-21 | Search Self-play ([2510.18821](https://arxiv.org/abs/2510.18821)) | 搜索智能体自博弈（SSP），EoG 机制母本 |
| 2025-08-07 | R-Zero ([2508.05004](https://arxiv.org/abs/2508.05004)) | Challenger/Solver 协同进化，伪标签 |
| 2025-05-06 | Absolute Zero ([2505.03335](https://arxiv.org/abs/2505.03335)) | 代码执行器验证的零数据自博弈 |

## Contributing

Suggestions and corrections are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, or use the paper-suggestion issue template.

## Scope and provenance

The initial collection was assembled using arXiv keyword searches, citation chasing from representative KGQA systems, and manual screening. Each annotation is based on the abstract and, when available, the paper's limitations/conclusion sections; it is not a substitute for a full-paper review.

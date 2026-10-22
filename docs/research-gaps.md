# Open research gaps in KGQA

These cross-paper observations were imported from the source survey and last reviewed on 2026-10-09. They are working research notes, not claims of exhaustive novelty; re-check the current literature before using them in a paper.

1. **"答对"≠"证据完整"仍缺训练信号。** RL 智能体主线（KG-R1、KnowCoder-A1、KBQA-R1、KG-Hopper、KG-Reasoner、SoG-R1、Temp-R1、TKG-Thinker）几乎都只用结果奖励或动作合法性奖励；TKG-Thinker 自己把"缺少中间过程评价"列为局限。补这个洞的只有 GAPD（需金逻辑形式）、RoP/SCPRM（学出来的奖励模型）、GraphCert（rubric，只在 GRBench）。**在 Freebase 规模 KG 上、用构造即正确的金三元组做步级信用分配，目前仍无人做**——这是 FoG 的位置，但 GraphCert 已非常接近，需要正面对比。
2. **过程监督依赖人工标注。** GAPD、SoG-R1、KG-TRACES、SALR 都要金 SPARQL/逻辑形式/路径；换一个没有标注的 KG 就用不了。
3. **合成数据的拓扑与捷径控制。** GraphWalker（随机游走）、GTSQA、GraphScout、GraphCert、Dynamic-KGQA 都没有检查"答案能否由证据真子集得到"；KGQAGen 指出现有人工基准事实正确率仅 57%。
4. **评测只看答案。** Theseus、The Path Matters、AGEE、MissDiag、Answer-Path 研究都在呼吁路径/证据级评测，但还没有被主流方法采纳的统一指标。
5. **不完整 KG。** 大量论文把"受 KG 完整性限制"写进局限（CoG、RoP、DeSQ、KG-Reasoner…）；Provenance Gap 与 Grounding-under-Incomplete-Evidence 说明"补全的边无法验证"是原理性难题。
6. **实体链接被默认给定。** SoG-R1、GRPO-DBLP、MetaQA 类工作都用 oracle 链接，端到端性能未知。
7. **跨 KG 迁移。** 绝大多数训练式方法只在 Freebase 上验证；KG-R1、KGFR、UltRAG、KGVoyager、PYTHIA 在做，但训练式智能体的跨 schema 迁移仍会退化。
8. **成本。** 免训练智能体普遍自述延迟/token 成本高且依赖闭源大模型——这是训练小模型路线的共同动机。

[Back to the paper list](../README.md)

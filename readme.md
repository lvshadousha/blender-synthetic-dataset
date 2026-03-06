blender-synthetic-dataset
用 Blender 4.4.3 生成合成数据集，目前输出为二值分割掩码

示例工程：hhhexperiment_model.blend  
渲染脚本：在 .blend 文件内部，文本名为 渲染脚本.py（直接在 Blender 中运行）

## 输出说明（Mask）
本项目当前输出的是二值掩码：

- 黑色 = 0（背景）
- 白色 = 1（目标/前景）

输出格式：PNG（纯黑白）

如果你后续需要 bbox、COCO/YOLO 标注：可以在渲染完成后，对 mask PNG 做脚本后处理（例如连通域提取 → bbox/面积/轮廓）。

## 环境要求
- Blender：4.4.3（建议与项目一致，避免 API/渲染差异）
- 操作系统：Windows / macOS / Linux 均可（以你的实际环境为准）

## 如何运行（Blender UI 内执行）
1. 使用 Blender 打开工程文件：hhhexperiment_model.blend
2. 打开 Scripting（脚本）工作区
3. 在文本编辑器（Text Editor）中找到脚本：渲染脚本.py
4. （强烈建议）先把渲染数量设置小一些进行测试
5. 点击 Run Script（运行脚本）执行

## 运行时注意事项
- 脚本执行后 Blender UI 会无响应（卡住）直到任务完成，属于预期现象。
- 建议首次运行：
  - 把渲染数量调到很小（例如 1～5 张）验证流程与输出路径无误
  - 确认输出目录可写、输出确实生成了 mask PNG
- 若需要更稳定的批量渲染体验，建议后续改为：
  - 后台模式（`blender -b ...`）运行，或
  - 在脚本中做分批渲染/定期保存/日志输出（按你的需求）

## 常见问题（FAQ）
### 1) 为什么我运行后 Blender 卡住了？
脚本执行期间会占用主线程/渲染资源，导致 UI 无响应，这是你当前脚本运行方式的正常表现。等任务完成后 UI 会恢复。



# 🎵 Music Sequencer with FastAPI

本项目是一个基于 **C 语言** 的音乐生成程序（music sequencer），并通过 **FastAPI** 封装为一个可调用的后端 API，实现从 note sequence 到 `.wav` 音频的自动生成。

---

## ✨ 功能特点

- 🎼 从 `.txt` 文件解析音符序列（note sequence）
- 🔊 使用 C 实现音频合成（audio synthesis）
- ⚡ 通过 **FastAPI** 提供 REST API 接口
- 🔗 将 **systems programming (C)** 与 **backend development (Python)** 结合

---

## ⚙️ 工作原理（Workflow）

1. C 程序读取输入的音符文件  
2. 根据 `note_frequencies.txt` 映射频率  
3. 使用 `NoteSynth` 模块生成 waveform  
4. 输出 `.wav` 音频文件  

FastAPI 部分负责：

- 调用 `gcc` 编译 C 程序  
- 使用 `subprocess` 执行程序  
- 返回生成的音频文件（FileResponse）

---

## 🚀 运行方式

安装依赖：
`pip install fastapi uvicorn`

启动服务：
`uvicorn api:app --reload`

访问接口：
`http://127.0.0.1:8000/generate`

自动生成并返回 .wav 音频

---

## 🧠 技术栈（Tech Stack）

- C（audio processing / systems programming）
- Python（FastAPI）
- GCC（compilation）
- REST API

---

👤 作者

田湛 （Zhan Tian)





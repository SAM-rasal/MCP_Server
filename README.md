MCP-Inspired AI Agent with Tool Calling

A practical implementation of **Model Context Protocol (MCP)** concepts using **Groq**, **LangChain**, and **LangGraph**. This project demonstrates how to build multi-server, multi-tool AI agents that can intelligently select and execute tools to solve problems.

## 🎯 Project Overview

This project consists of:

- ✅ **Model Context Protocol Architecture** - Communication between LLM and tools
- ✅ **Tool Servers** - Multiple tool servers (Math, Weather) exposing capabilities
- ✅ **Tool Discovery** - Agent discovers available tools and their schemas
- ✅ **Intelligent Tool Selection** - Agent chooses correct tools for tasks
- ✅ **Function Calling** - Executing tools with proper parameters
- ✅ **Multi-Tool Workflows** - Chaining multiple tool calls
- ✅ **ReAct Pattern** - Reasoning and Acting for problem solving
- ✅ **Async Communication** - FastMCP servers with streamable-http transport

MCP Architecture

What is Model Context Protocol (MCP)?

MCP is a **standardized protocol** for communication between AI models and tools/services. It defines:

1. **Servers** - Expose tools/resources/prompts
2. **Clients** - Connect to servers and get tools
3. **Transport** - How servers and clients communicate (stdio, HTTP, WebSocket)
4. **Schema** - Tool definitions with parameters and descriptions

### Your Project Architecture

┌──────────────────────────────────────────────────┐
│ LLM Agent (client.py) │
│ - LangChain + LangGraph Integration │
│ - Groq LLaMA 3.1 8B (Fast Inference) │
│ - ReAct Pattern Implementation │
└──────────────────────┬───────────────────────────┘
│
┌─────────────┴──────────────┐
│ │
┌────▼─────────┐ ┌────────▼──────────┐
│ Math Server │ │ Weather Server │
│ (MCP Server) │ │ (MCP Server) │
│ │ │ │
│ Transport: │ │ Transport: │
│ stdio │ │ streamable-http │
│ │ │ │
│ Tools: │ │ Tools: │
│ - add() │ │ - get_weather() │
│ - multiply() │ │ │
└──────────────┘ └────────────────────┘
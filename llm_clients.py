#!/usr/bin/env python3
"""
Enhanced LLM Client for Quarto Presentation Generator using LangChain

This module provides unified LLM integration using LangChain framework.
"""

import os
from typing import Optional
from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


class LangChainLLMClient:
    """Unified LLM client using LangChain framework"""

    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.client = self._create_client(model)
        self.system_prompt = "You are an expert presentation designer specializing in educational content and Quarto RevealJS presentations."

    def _create_client(self, model: str) -> BaseChatModel:
        """Create appropriate LangChain chat model based on model name"""

        # OpenAI models
        if model.startswith(("gpt-", "text-")) or model in ["gpt-4", "gpt-3.5-turbo"]:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable.")
            return ChatOpenAI(
                model=model,
                api_key=api_key,
                temperature=0.7,
                max_tokens=2000
            )

        # Anthropic Claude models
        elif model.startswith("claude-"):
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("Anthropic API key required. Set ANTHROPIC_API_KEY environment variable.")
            return ChatAnthropic(
                model=model,
                api_key=api_key,
                temperature=0.7,
                max_tokens=2000
            )

        # Local models (Ollama)
        else:
            # Assume it's a local Ollama model
            return ChatOllama(
                model=model,
                temperature=0.7,
                num_predict=2000
            )

    def generate_response(self, prompt: str) -> str:
        """Generate response using LangChain chat model"""
        try:
            messages = [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=prompt)
            ]

            response = self.client.invoke(messages)
            return response.content.strip()

        except Exception as e:
            print(f"❌ LLM API error: {e}")
            return self._fallback_response(prompt)

    def _fallback_response(self, prompt: str) -> str:
        """Provide fallback response if API fails"""
        if "general structure" in prompt.lower():
            return '''
            {
                "title": "Article Analysis Presentation",
                "slides": [
                    {"slide_number": 1, "title": "Introduction", "type": "intro", "key_points": ["Welcome", "Overview", "Objectives"]},
                    {"slide_number": 2, "title": "Main Topic", "type": "content", "key_points": ["Key concept", "Background"]},
                    {"slide_number": 3, "title": "Analysis", "type": "content", "key_points": ["Deep dive", "Examples"]},
                    {"slide_number": 4, "title": "Conclusion", "type": "conclusion", "key_points": ["Summary", "Takeaways"]}
                ]
            }
            '''
        else:
            return "## Fallback Slide\n\n- Content generation failed\n- Using fallback response\n- Please review and edit"


# Backward compatibility aliases
OpenAIClient = LangChainLLMClient
AnthropicClient = LangChainLLMClient
LocalLLMClient = LangChainLLMClient


# Example usage and integration instructions
if __name__ == "__main__":
    print("🔧 LangChain LLM Client Integration Guide")
    print("\nNow using LangChain framework for unified LLM integration!")
    print("\nSupported models:")
    print("- OpenAI: gpt-4, gpt-3.5-turbo")
    print("- Anthropic: claude-3-sonnet-20240229, claude-3-haiku-20240307")
    print("- Local (Ollama): llama2, codellama, etc.")

    print("\nSet up your API keys:")
    print("   export OPENAI_API_KEY='your-key-here'")
    print("   export ANTHROPIC_API_KEY='your-key-here'")

    print("\nInstall required dependencies:")
    print("   pip install langchain langchain-openai langchain-anthropic langchain-ollama")

    # Test if API keys are available
    print("\n🔍 Checking API keys:")
    if os.getenv("OPENAI_API_KEY"):
        print("✅ OpenAI API key found")
    else:
        print("❌ OpenAI API key not found")

    if os.getenv("ANTHROPIC_API_KEY"):
        print("✅ Anthropic API key found")
    else:
        print("❌ Anthropic API key not found")

import os

import pytest
from langchain_core.language_models import BaseChatModel


def _create_openai_llm() -> BaseChatModel:
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
    )


def _create_anthropic_llm() -> BaseChatModel:
    from langchain_anthropic import ChatAnthropic

    return ChatAnthropic(
        model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514"),
        temperature=0,
    )


LLM_PROVIDERS = {
    "openai": _create_openai_llm,
    "anthropic": _create_anthropic_llm,
}


@pytest.fixture
def llm() -> BaseChatModel:
    """
    Provides a configured LLM for testing.

    Configuration via environment variables:
    - LLM_PROVIDER: "openai" (default) or "anthropic"
    - OPENAI_API_KEY: Required when using OpenAI
    - OPENAI_MODEL: Model name (default: "gpt-4o-mini")
    - ANTHROPIC_API_KEY: Required when using Anthropic
    - ANTHROPIC_MODEL: Model name (default: "claude-sonnet-4-20250514")
    """
    provider = os.environ.get("LLM_PROVIDER", "openai").lower()

    if provider not in LLM_PROVIDERS:
        raise ValueError(
            f"Unknown LLM_PROVIDER: {provider}. "
            f"Supported providers: {', '.join(LLM_PROVIDERS.keys())}"
        )

    return LLM_PROVIDERS[provider]()

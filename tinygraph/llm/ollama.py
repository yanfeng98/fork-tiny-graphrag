from ollama import chat
from ollama import ChatResponse
from typing import Any, Optional
from .base import BaseLLM


class ollamaLLM(BaseLLM):
    """Implementation of the BaseLLM interface using ollama."""

    def __init__(
        self,
        model_name: str,
        model_params: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        super().__init__(model_name, model_params, **kwargs)

    def predict(self, input: str) -> str:
        """Sends a text input to the ollama model and retrieves a response.

        Args:
            input (str): Text sent to the ollama model

        Returns:
            str: The response from the ollama model.
        """
        response: ChatResponse = chat(
            model=self.model_name,
            messages=[
                {
                    'role': 'user',
                    'content': input,
                },
            ]
        )
        return response.message.content

"""Session list item"""
from __future__ import annotations

from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label
from textual.widgets import ListItem

from parllama.models.chat import ChatSession


class SessionListItem(ListItem, can_focus=False, can_focus_children=True):
    """Session list item"""

    DEFAULT_CSS = """
    SessionListItem {
      height: 4;
      width: 1fr;
      padding-left: 1;
      padding-right: 1;
    }
    """
    session: ChatSession

    def __init__(self, session: ChatSession, **kwargs) -> None:
        """Initialise the view."""
        super().__init__(**kwargs)
        self.session = session

    def compose(self) -> ComposeResult:
        """Compose the content of the view."""
        with Vertical():
            yield Label(self.session.session_name)
            temp = (
                f"{self.session.options['temperature']:.2f}"
                if self.session.options.get("temperature") is not None
                else "Default"
            )

            yield Label(
                Text.assemble(self.session.llm_model_name, " ", f"Temp: {temp}")
            )
            yield Label(
                Text.assemble(
                    "Last updated: ",
                    self.session.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
                )
            )
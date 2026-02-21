"""Terminal UI engine with colors, animations, and rich formatting."""

import os
import sys
import time
import shutil
import textwrap


# ANSI color codes
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    STRIKE = "\033[9m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


def get_width():
    return min(shutil.get_terminal_size().columns, 100)


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def print_centered(text, color=""):
    w = get_width()
    for line in text.split("\n"):
        stripped = _strip_ansi(line)
        pad = max(0, (w - len(stripped)) // 2)
        print(" " * pad + color + line + C.RESET)


def _strip_ansi(text):
    import re
    return re.sub(r'\033\[[0-9;]*m', '', text)


def hr(char="─", color=C.BRIGHT_BLACK):
    print(f"{color}{char * get_width()}{C.RESET}")


def hr_fancy(label="", color=C.CYAN):
    w = get_width()
    if label:
        label_str = f" {label} "
        side = (w - len(label_str)) // 2
        print(f"{color}{'━' * side}{C.BOLD}{label_str}{C.RESET}{color}{'━' * (w - side - len(label_str))}{C.RESET}")
    else:
        print(f"{color}{'━' * w}{C.RESET}")


def box(text, color=C.CYAN, padding=2):
    w = get_width() - 4
    lines = []
    for line in text.split("\n"):
        wrapped = textwrap.wrap(line, w - padding * 2) or [""]
        lines.extend(wrapped)

    print(f"{color}╭{'─' * (w + 2)}╮{C.RESET}")
    for line in lines:
        stripped = _strip_ansi(line)
        pad_right = w - len(stripped)
        print(f"{color}│{C.RESET} {line}{' ' * max(0, pad_right)} {color}│{C.RESET}")
    print(f"{color}╰{'─' * (w + 2)}╯{C.RESET}")


def info_box(title, content, color=C.BLUE):
    w = get_width() - 4
    print(f"\n{color}┌{'─' * (w + 2)}┐{C.RESET}")
    title_stripped = _strip_ansi(title)
    pad = w - len(title_stripped)
    print(f"{color}│ {C.BOLD}{title}{C.RESET}{' ' * max(0, pad)} {color}│{C.RESET}")
    print(f"{color}├{'─' * (w + 2)}┤{C.RESET}")
    for line in content.split("\n"):
        wrapped = textwrap.wrap(line, w - 2) or [""]
        for wl in wrapped:
            stripped = _strip_ansi(wl)
            pad = w - len(stripped)
            print(f"{color}│ {C.RESET}{wl}{' ' * max(0, pad)} {color}│{C.RESET}")
    print(f"{color}└{'─' * (w + 2)}┘{C.RESET}")


def type_text(text, delay=0.015, color=""):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def slow_print(text, delay=0.005, color=""):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_command(cmd, description=""):
    w = get_width()
    cmd_display = f"  {C.BRIGHT_GREEN}{C.BOLD}{cmd}{C.RESET}"
    if description:
        print(f"{cmd_display}")
        print(f"    {C.DIM}{description}{C.RESET}")
    else:
        print(cmd_display)


def print_shortcut(keys, description):
    print(f"  {C.BRIGHT_YELLOW}{C.BOLD}{keys:<22}{C.RESET} {C.WHITE}{description}{C.RESET}")


def print_tip(text):
    print(f"\n  {C.BRIGHT_YELLOW}💡 TIP:{C.RESET} {C.WHITE}{text}{C.RESET}")


def print_warning(text):
    print(f"\n  {C.BRIGHT_RED}⚠️  WARNING:{C.RESET} {C.WHITE}{text}{C.RESET}")


def print_success(text):
    print(f"\n  {C.BRIGHT_GREEN}✅ {text}{C.RESET}")


def print_error(text):
    print(f"\n  {C.RED}❌ {text}{C.RESET}")


def print_xp(amount, reason=""):
    if reason:
        print(f"  {C.BRIGHT_MAGENTA}⭐ +{amount} XP{C.RESET} {C.DIM}— {reason}{C.RESET}")
    else:
        print(f"  {C.BRIGHT_MAGENTA}⭐ +{amount} XP{C.RESET}")


def print_achievement(name, desc=""):
    print(f"\n  {C.BRIGHT_YELLOW}🏆 ACHIEVEMENT UNLOCKED: {C.BOLD}{name}{C.RESET}")
    if desc:
        print(f"     {C.DIM}{desc}{C.RESET}")
    print()


def print_level_up(old_level, new_level, title):
    print()
    hr_fancy("LEVEL UP!", C.BRIGHT_YELLOW)
    print_centered(f"{C.BRIGHT_YELLOW}{C.BOLD}Level {old_level} → Level {new_level}{C.RESET}")
    print_centered(f"{C.BRIGHT_CYAN}{title}{C.RESET}")
    hr_fancy("", C.BRIGHT_YELLOW)
    print()


def progress_bar(current, total, width=30, label="", color=C.GREEN):
    filled = int(width * current / total) if total > 0 else 0
    bar = f"{color}{'█' * filled}{C.BRIGHT_BLACK}{'░' * (width - filled)}{C.RESET}"
    pct = int(100 * current / total) if total > 0 else 0
    if label:
        print(f"  {label} {bar} {pct}% ({current}/{total})")
    else:
        print(f"  {bar} {pct}% ({current}/{total})")


def menu(options, prompt="Choose", back_option=True, color=C.CYAN):
    print()
    valid_indices = {}
    num = 1
    for label, val in options:
        if not label:
            print()
            continue
        valid_indices[num] = val
        print(f"  {color}{C.BOLD}{num}.{C.RESET} {label}")
        num += 1
    if back_option:
        print(f"  {C.DIM}0. ← Back{C.RESET}")
    print()
    max_num = num - 1
    while True:
        try:
            choice = input(f"  {C.BRIGHT_WHITE}{prompt} ▸ {C.RESET}").strip()
            if choice == "0" and back_option:
                return None
            if choice == "q":
                return "quit"
            idx = int(choice)
            if idx in valid_indices:
                return valid_indices[idx]
        except (ValueError, EOFError):
            pass
        print(f"  {C.DIM}Enter 1-{max_num}{' or 0 to go back' if back_option else ''}{C.RESET}")


def confirm(prompt="Continue?"):
    try:
        resp = input(f"\n  {C.BRIGHT_WHITE}{prompt} (y/n) ▸ {C.RESET}").strip().lower()
        return resp in ("y", "yes", "")
    except EOFError:
        return False


def pause(msg="Press Enter to continue..."):
    try:
        input(f"\n  {C.DIM}{msg}{C.RESET}")
    except EOFError:
        pass


def print_scenario(title, description):
    print(f"\n  {C.BRIGHT_CYAN}📋 SCENARIO: {C.BOLD}{title}{C.RESET}")
    print()
    for line in description.split("\n"):
        print(f"    {C.WHITE}{line}{C.RESET}")
    print()


def print_difficulty(level):
    colors = {
        "beginner": (C.GREEN, "🟢"),
        "intermediate": (C.YELLOW, "🟡"),
        "advanced": (C.RED, "🔴"),
        "expert": (C.BRIGHT_MAGENTA, "💎"),
    }
    color, icon = colors.get(level, (C.WHITE, "⚪"))
    print(f"  {icon} {color}{C.BOLD}{level.upper()}{C.RESET}")


BANNER = r"""
   ██████╗ ██████╗ ██████╗ ██╗██╗      ██████╗ ████████╗
  ██╔════╝██╔═══██╗██╔══██╗██║██║     ██╔═══██╗╚══██╔══╝
  ██║     ██║   ██║██████╔╝██║██║     ██║   ██║   ██║
  ██║     ██║   ██║██╔═══╝ ██║██║     ██║   ██║   ██║
  ╚██████╗╚██████╔╝██║     ██║███████╗╚██████╔╝   ██║
   ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝    ╚═╝

   ██████╗██╗     ██╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ ██╗   ██╗
  ██╔════╝██║     ██║    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗ ██╔╝
  ██║     ██║     ██║    ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝ ╚████╔╝
  ██║     ██║     ██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗  ╚██╔╝
  ╚██████╗███████╗██║    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║   ██║
   ╚═════╝╚══════╝╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝
"""


def show_splash():
    clear()
    print_centered(BANNER, C.BRIGHT_CYAN)
    print_centered(f"{C.BRIGHT_WHITE}{C.BOLD}The Interactive Training System for GitHub Copilot CLI{C.RESET}")
    print_centered(f"{C.DIM}v1.0 — From Zero to CLI Wizard{C.RESET}")
    print()
    hr_fancy("", C.CYAN)
    print()

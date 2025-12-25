# Study Planner - Focus-based CLI tool
# Author: Sayam
# Language: Python

from datetime import datetime

MAX_FOCUS_HOURS = 4.5
FOCUS_BLOCK = 50  # minutes
BREAK_TIME = 10   # minutes


def print_header():
    print("\n" + "=" * 45)
    print("        📘 FOCUS-BASED STUDY PLANNER")
    print("        Plan less. Execute more.")
    print("=" * 45 + "\n")


def get_tasks():
    tasks = []
    while True:
        subject = input("Subject name (or 'done'): ").strip()
        if subject.lower() == "done":
            break

        try:
            minutes = int(input("Time required (minutes): "))
        except ValueError:
            print("❌ Enter time in numbers only.\n")
            continue

        priority = input("Priority (High / Medium / Low): ").strip().capitalize()
        deadline = input("Deadline (optional): ").strip()

        tasks.append({
            "subject": subject,
            "minutes": minutes,
            "priority": priority,
            "deadline": deadline
        })
        print("✔ Task added.\n")

    return tasks


def priority_score(priority):
    return {"High": 1, "Medium": 2, "Low": 3}.get(priority, 4)


def analyze_tasks(tasks):
    total_minutes = sum(task["minutes"] for task in tasks)
    total_hours = round(total_minutes / 60, 2)

    print("\n" + "-" * 45)
    print("📊 STUDY REALITY CHECK")
    print("-" * 45)
    print(f"Planned study time: {total_hours} hours")

    if total_hours > MAX_FOCUS_HOURS:
        print("⚠ WARNING: This plan is unrealistic.")
        print(f"✔ Recommended focus limit: {MAX_FOCUS_HOURS} hours")
    else:
        print("✔ This plan is realistic.")

    return total_minutes


def generate_focus_plan(tasks):
    print("\n" + "-" * 45)
    print("🧠 FOCUS PLAN")
    print("-" * 45)

    tasks.sort(key=lambda x: priority_score(x["priority"]))

    for task in tasks:
        blocks = task["minutes"] // FOCUS_BLOCK
        remainder = task["minutes"] % FOCUS_BLOCK

        print(f"\n🔥 {task['subject']} ({task['priority']} Priority)")
        for i in range(blocks):
            print(f"  • Study {FOCUS_BLOCK} min → Break {BREAK_TIME} min")

        if remainder > 0:
            print(f"  • Study {remainder} min (final session)")

        if task["deadline"]:
            print(f"    ⏳ Deadline: {task['deadline']}")


def main():
    print_header()
    tasks = get_tasks()

    if not tasks:
        print("No tasks entered. Exiting.")
        return

    analyze_tasks(tasks)
    generate_focus_plan(tasks)

    print("\n" + "=" * 45)
    print("Done. Now stop planning and start studying.")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()
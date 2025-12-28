def analyze(data):
    timeline = []
    score = 0

    for i, a in enumerate(data.attempts):
        progress = 100 if a.success else min(90, 30 + i * 20)
        timeline.append({
            "attempt": i + 1,
            "progress": progress,
            "issue": a.error if not a.success else None
        })
        score = max(score, progress)

    return {
        "timeline": timeline,
        "final_score": score
    }

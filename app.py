from typing import List

def analyze_code(data: dict):
    # Example structure: data = {"attempts": [{"code": "...", "success": True}, ...]}
    attempts = data.get("attempts", [])
    progress_scores = []
    for i, a in enumerate(attempts):
        progress = 100 if a.get("success") else min(90, i * 20)
        progress_scores.append(progress)
    final_score = max(progress_scores) if progress_scores else 0
    return {
        "timeline": progress_scores,
        "final_score": final_score
    }

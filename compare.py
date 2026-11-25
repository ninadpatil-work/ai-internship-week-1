required_skills = {"python", "sql", "git", "fastapi"}
candidate_skills = {"python", "sql", "docker", "pandas"}

print(required_skills | candidate_skills)  # Union: all unique skills in either set
print(required_skills & candidate_skills)  # Intersection: {'python', 'sql'} (common)
print(required_skills - candidate_skills)  # Difference: {'git', 'fastapi'} (missing)
print(required_skills ^ candidate_skills)  # Symmetric difference: in one set, not both
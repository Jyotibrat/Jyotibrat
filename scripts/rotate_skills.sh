#!/bin/bash

# Define paths
README="src/README.md"
TEMPLATES_DIR="templates"

# Get the total number of skill files
NUM_TEMPLATES=$(ls "$TEMPLATES_DIR"/skills_*.md | wc -l)

# Get the current timestamp in minutes
CURRENT_MIN=$(date +%M)

# Calculate which template to use based on time
INDEX=$(( (CURRENT_MIN / 5) % NUM_TEMPLATES + 1 ))

# Select the corresponding skills file
SKILLS_FILE="$TEMPLATES_DIR/skills_${INDEX}.md"

# Extract content before the Skills section
sed -n '1,/<!-- SKILLS_SECTION_START -->/ p' "$README" > temp_readme.md

# Add the new Skills section
echo "<!-- SKILLS_SECTION_START -->" >> temp_readme.md
cat "$SKILLS_FILE" >> temp_readme.md
echo "<!-- SKILLS_SECTION_END -->" >> temp_readme.md

# Extract content after the Skills section
sed -n '/<!-- SKILLS_SECTION_END -->/,$ p' "$README" >> temp_readme.md

# Replace old README with updated content
mv temp_readme.md "$README"

# Commit and push changes
git config --global user.name "github-actions"
git config --global user.email "github-actions@github.com"
git add "$README"
git commit -m "Updated Skills & Technologies section (auto-update)"
git push

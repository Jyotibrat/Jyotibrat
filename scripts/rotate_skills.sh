#!/bin/bash

# Define paths
README="src/README.md"   # Adjusted path for README
TEMPLATES_DIR="templates"

# Get the total number of skill files
NUM_TEMPLATES=$(ls "$TEMPLATES_DIR"/skills_*.md | wc -l)

# Get the current timestamp in minutes
CURRENT_MIN=$(date +%M)

# Calculate which template to use based on time
INDEX=$(( (CURRENT_MIN / 5) % NUM_TEMPLATES + 1 ))

# Select the corresponding skills file
SKILLS_FILE="$TEMPLATES_DIR/skills_${INDEX}.md"

# Replace the old skills section in README
sed -i '/## 🛠️ Skills & Technologies/,$d' "$README"  # Remove existing section
cat "$SKILLS_FILE" >> "$README"                      # Append new section

# Commit and push changes
git config --global user.name "github-actions"
git config --global user.email "github-actions@github.com"
git add "$README"
git commit -m "Updated Skills & Technologies section (auto-update)"
git push

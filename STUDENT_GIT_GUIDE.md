# Git Workflow for Students

## 1. Clone the `students` branch

Replace `<REPOSITORY_URL>` with the URL of the Git repository:

```bash
git clone -b students --single-branch <REPOSITORY_URL>
```

Then move into the cloned project folder:

```bash
cd <PROJECT_FOLDER>
```

## 2. Create your own group branch

Create a new branch called `group_01` and switch to it:

```bash
git switch -c group_01
```

For other groups, use a different branch name, for example `group_02`, `group_03`, and so on.

## 3. Save and push your changes

After making changes to the project, add all changed files:

```bash
git add .
```

Create a commit with a short message describing your changes:

```bash
git commit -m "Describe your changes here"
```

The first time you push your new group branch, use:

```bash
git push -u origin group_01
```

After that, future changes can be pushed with:

```bash
git add .
git commit -m "Describe your changes here"
git push
```

# Pack Architecture

## 1. Purpose

The Universal SDLC Agent Skills Pack is a modular, portable system that helps AI coding agents turn software-work requests into well-defined engineering work and verifiable results. It combines curated skills, workflow contracts, artifact templates, package metadata, and runtime adapters.

The governing principle is **flexible input, disciplined output**. A task may begin with a plain-language request, partial context, an existing codebase, a confirmed stack, or a detailed specification. The pack must not require a complete intake form or `STACK.md` before useful work can begin. It must make the expected outcome, constraints, assumptions, and verification status explicit, and must never hide uncertainty or claim checks that were not performed.

The pack supports SDLC work; it does not impose every stage or deliverable on every project.

## 2. Architectural Principles

- **Input flexibility:** use whatever reliable context is available. Ask for clarification only when missing information materially affects correctness, safety, or acceptance; otherwise proceed with explicit assumptions.
- **Output contracts:** define observable expectations for the result, relevant deliverables, acceptance criteria, and verification. Incomplete inputs may lead to an assumption, partial result, or blocked status—not fabricated facts or silently weakened criteria.
- **Modular responsibilities:** keep skills, orchestration, artifact contracts, catalogs, and runtime integration independently maintainable behind clear interfaces.
- **One source of truth per concern:** each canonical fact has one authoritative owner. Derived views may be duplicated for readability only when consistency can be checked.
- **Demand-driven task context:** select the smallest sufficient set of skills based on task demands and expand incrementally as needed, rather than enforcing a rigid numerical limit. This is a selection target, not a guarantee that every runtime can load only those skills; runtime behavior must be reported accurately.
- **Honest implementation status:** distinguish implemented behavior, manual procedure, and target capability. Documentation must not imply automation exists unless the repository actually implements and tests it.

## 3. Core Concepts and Sources of Truth

- **Master Matrix** (`sdlc-practical-matrix.md`): a curated reference for important SDLC stages, responsibility groups, artifacts, competencies, and representative skills. It is not the packaged inventory, a mandatory checklist, or a runtime loading list.
- **Packaged Inventory:** the skills actually distributed by the repository. The manifest is authoritative for machine-readable package identity and metadata; inventory listings are derived views of that data and the package files, not a competing source of truth.
- **Stable Skill ID:** an identifier that remains stable across changes to display name or source path where continuity is intended. Names and paths are metadata, not reliable identifiers by themselves.
- **Core / Extras:** classifications of packaged skills. Core identifies baseline capabilities intended for broad use and default installation; Extras identifies context-dependent capabilities for particular stacks, domains, roles, infrastructure, or compliance needs. Neither classification means the skills must all be loaded into every task context.
- **Project Skill Set:** the skills selected as relevant to a project from its known context. It is useful when project context persists, but it is optional and must not be a prerequisite for handling a standalone task.
- **Task Active Skills:** the set selected and loaded for the current task based on demand. Selection, runtime availability, context loading, and actual activation/use are distinct states and must not be conflated.
- **`STACK.md`:** an optional structured input describing a confirmed or proposed stack and related constraints. Other reliable sources, including a user request or repository inspection, may provide enough context without it.
- **Artifact Contract:** the canonical definition of a deliverable's purpose, required properties, acceptance criteria, and verification. Each artifact type has one authoritative contract. A template instantiates that contract; a workflow coordinates its production and checks; a skill supplies the domain work.

## 4. Two Related Flows

### 4.1 Pack Development and Distribution

`Sources → Curation & Verification → Packaged Inventory → Classification → Release / Distribution`

1. **Sources:** upstream or local skills and reference material.
2. **Curation & Verification:** validate provenance, current content, distinct value, safety, license/usage terms where applicable, and runtime compatibility.
3. **Packaged Inventory:** record accepted packages and their stable IDs, source/revision metadata, content hashes, and relevant constraints.
4. **Classification:** assign Core or Extras to packaged skills according to the documented policy.
5. **Release / Distribution:** package and make the accepted version available for installation or use.

The Master Matrix informs curation but does not require every listed skill to be packaged. A skill is not available merely because it appears in the matrix or an external catalog.

### 4.2 Project Provisioning and Task Execution

Project provisioning, when useful:

`Available Project Context + Packaged Inventory → Project Skill Set → Optional Installation`

Task execution:

`Task Request + Available Context → Normalized Task Context → Task Contract → Skill Selection → Runtime Provisioning → Execution → Verification → Completion Report`

- **Normalize context:** identify the goal, constraints, confirmed facts, evidence-based inferences, assumptions, and material unknowns. Reuse known context rather than forcing it into a rigid intake form.
- **Define the task contract:** state the intended outcome, applicable output contract, acceptance criteria, and needed checks. Keep it lightweight and internal for simple tasks; persist it when the task's complexity or collaboration needs justify it.
- **Select skills:** prefer the Project Skill Set when it exists. For a standalone task or a project without a prepared set, select directly from the Packaged Inventory using the task context. Do not create a project profile solely to perform a simple task.
- **Provision skills:** determine which selected skills are available to the runtime and how they are exposed. Load full instructions only for the selected skills when the runtime supports selective loading.
- **Execute and verify:** use the chosen skills and applicable project conventions, then check the result against the task contract. Revisit selection or earlier steps when new evidence materially changes the task.
- **Report honestly:** state what was completed, what was checked, the evidence available, and any unresolved limitation. If no suitable skill is available, proceed without pretending one was used, when safe and reasonable; otherwise report the blocker.

This is a logical workflow, not a mandatory linear SDLC process. Steps may be skipped, repeated, or revisited according to the task.

### 4.3 Demand-Driven Skill Loading

The pack must support demand-driven skill discovery, selection, and loading without a fixed numerical limit on active skills.

Installation determines which skills are available in the target agent environment. Runtime selection determines which skills are relevant to the current task. Context loading and activation load the instructions needed to execute the work. These are separate concerns:

| Layer | Responsibility |
| --- | --- |
| **Installation** | Determines which skills are installed and available in the target agent environment (can install all packaged skills). |
| **Skill Discovery & Selection** | Identifies and selects skills based on task requirements, context, complexity, dependencies, and scope. |
| **Context Loading & Activation** | Loads instructions for selected skills; allows incremental loading of additional skills when new subtasks or requirements emerge, if the runtime supports it. |

The execution lifecycle operates as a demand-driven feedback loop:

1. **Task Intake:** Ingest task request, available context, confirmed constraints, and target outcomes.
2. **Discover & Select:** Identify relevant skills from the inventory; determine dependencies and execution boundaries.
3. **Load & Execute:** Load the smallest sufficient set of skill instructions and proceed with the workflow.
4. **Reassess & Expand:** If a subtask emerges or a capability gap is encountered, discover and load additional skills dynamically rather than being constrained by an initial guess.
5. **Verify Output Contract:** Check the final results against the applicable artifact and task contracts.

The system should avoid unnecessary context loading, redundant instructions, and conflicting skill guidance. It must not enforce a universal skill-count limit such as one to three skills.

Adapters must describe the actual loading and activation capabilities of each runtime. When dynamic loading is unavailable, the pack must use an explicitly documented fallback rather than claiming selective or incremental loading that has not been implemented.

Skill selection and loading do not establish task completion. Final outputs remain subject to their applicable output contracts and verification requirements.

## 5. Output Contracts

Output contracts are the pack's primary quality control. Their strictness applies to what counts as a valid result—not to how much information the user must provide up front.

### 5.1 Minimum Completion Contract

Every task completion report must communicate, at a level proportional to the task:

- **Status:** `completed`, `partially completed`, `blocked`, or `failed`.
- **Result:** the deliverable or outcome actually produced, with links or paths where applicable.
- **Acceptance and verification:** the relevant criteria checked and the evidence or test results available. Clearly distinguish checks performed from checks recommended or not run.
- **Limitations:** material assumptions, unresolved questions, failures, or follow-up required.

This contract does not require a persistent document for every task. For example, a small code edit may need a concise summary and test result; a design task may need decisions and trade-offs; a research task may need sources and uncertainty; a planning task may need ordered, actionable items.

### 5.2 Specialized Artifact Contracts

Each important artifact type (for example, a requirements specification, task plan, ADR, or test report) must have one canonical contract defining its required properties and acceptance criteria. The owning contract must be referenced rather than independently redefined by every skill.

- **Contract owner:** defines the canonical structure and acceptance requirements for that artifact type.
- **Template:** provides a reusable starting structure consistent with the contract; it may mark fields required or optional.
- **Workflow:** coordinates the steps, handoffs, and validation needed to produce the artifact.
- **Skill:** performs the relevant domain work and produces outputs that satisfy the applicable contract.
- **Schema or validator:** checks machine-readable structure where feasible; human-readable artifacts are checked against explicit criteria.

Contracts may be extended for a specific workflow, but extensions must not silently conflict with canonical requirements. Project conventions may refine defaults unless they violate an explicit task requirement or higher-priority constraint.

## 6. Design and Extension Patterns

Use a pattern only when it solves a real coupling, change, or consistency problem. These are design choices, not a checklist of abstractions to implement.

- **Ports and Adapters:** keep core concepts and policies independent of agent runtimes, source hosts, and installation destinations. Runtime-specific paths and commands belong in adapters.
- **Registry / Catalog:** consumers use the authoritative manifest-backed inventory to determine what is packaged and available; they must not infer availability from the Master Matrix or folder names alone.
- **Strategy:** skill-selection policy can evolve—from manual selection to rule-based or automated selection—without changing the underlying catalog and output contracts.
- **Workflow orchestration pipeline:** normalize context, form the task contract, select skills, execute, and verify as distinct responsibilities. Allow branching, retries, and returning to earlier steps when new evidence appears. This is a pipeline with control flow, not a mandatory linear process or an assumed Chain of Responsibility implementation.
- **Composition:** assemble workflows from focused skills, contracts, templates, and checks instead of duplicating procedures in one monolithic skill.
- **Contract-first validation:** version important machine-readable contracts and validate them against schemas where feasible; test human-readable outputs against acceptance criteria.
- **Staged, recoverable updates:** stage source syncs, package changes, and installation updates; review diffs and validate before replacing accepted state. Updates and installation should be non-destructive by default.

Avoid abstractions that have no current consumer. A new runtime or provider should normally require an adapter and configuration, not changes throughout core policy.

## 7. Logical Repository Responsibilities

These describe responsibilities, not a claim that every directory or automation already exists. Keep this map aligned with the actual repository; do not create empty directories merely to match the document.

- `skills/`: self-contained skill packages and supporting references/assets. Upstream content stays close to source where practical; local adaptations are explicit.
- `workflows/`: pack-level coordination, entry conditions, handoffs, transitions, and checks. Do not copy entire skill procedures into workflows.
- `templates/`: reusable, agent-neutral artifact structures aligned with canonical contracts.
- `adapters/`: runtime-specific configuration, capability declarations, path mappings, and installation behavior. Adapters do not own canonical SDLC policy.
- `manifests/`: authoritative machine-readable records for packaged skills, stable IDs, provenance, revisions, hashes, classifications, and applicable compatibility metadata.
- `scripts/`: tooling for synchronization, validation, packaging, release, and installation/update operations where implemented.
- `schemas/` and `tests/` (or equivalent): schemas and checks for manifests, contracts, package integrity, selection behavior, runtime compatibility, and installation safety where present or needed.

When describing a component or capability, mark it as **implemented**, **manual**, or **target** when that distinction is material. Do not document a proposed path or tool as existing without checking the repository.

## 8. Governance and Quality Gates

### 8.1 Source and Package Governance

- **Upstream / sync-managed:** external skills retained close to their source and pinned to an identifiable revision.
- **Locally adapted:** skills modified for the pack, with source, revision, adaptation rationale, and content hash recorded.
- **Reference-only:** material informing the matrix, templates, or decisions but not distributed as executable skill content.

Before inclusion or update, verify the canonical repository and exact skill path, inspect current instructions, check for deprecated or renamed versions, assess distinct value and safety, and record applicable license/usage terms and compatibility constraints. Do not execute suspicious instructions while reviewing them. Popularity and installation counts are secondary signals, not proof of quality, safety, or suitability.

### 8.2 Quality Gates

Apply the relevant gates to each change and report which are automated versus manual:

- **Content and safety:** clear purpose, bounded scope, no unjustified or unacceptable side effects.
- **Provenance and integrity:** real source/path, stable identity, accurate revision and hash, package files consistent with manifest.
- **Contract integrity:** valid machine-readable schemas and explicit acceptance criteria for important outputs.
- **Composition integrity:** valid references, no unnecessary duplication or circular dependencies, and compatible contract changes.
- **Runtime and installation:** only claim compatibility for tested runtimes; updates are reviewable, repeatable, and non-destructive by default.
- **Task-result integrity:** reports match the work performed and evidence available, including failed or skipped checks.

Structural validation does not substitute for a formal security audit, legal clearance, or empirical evaluation across agent runtimes. Never claim a gate passed unless it was actually checked.

## 9. Evolving the Pack Like Software

### Add or update a skill

1. Identify a concrete capability need using the Master Matrix as a reference, not as automatic approval to package a listed skill.
2. Verify source, exact path, current instructions, revision, usage terms, safety, compatibility, and maintenance status.
3. Compare with existing packages and record why it adds distinct value or replaces an existing skill.
4. Stage the change without overwriting the currently accepted version; update the authoritative manifest and affected references.
5. Run available checks, inspect the content diff, and update relevant tests or documentation.
6. Review compatibility and migration impact. Release only when required checks pass; record unresolved checks explicitly.

### Add a runtime or source provider

Implement the required adapter contract and declare the runtime's actual capabilities, including how skills are discovered, made available, loaded, and invoked. Do not assume all runtimes support selective loading. If a runtime exposes more skills than selected, report that limitation and avoid claiming a strict context limit.

### Change a contract or component

Identify dependent skills, workflows, templates, adapters, schemas, and tests. Update them together, version breaking changes where necessary, and provide migration guidance. Avoid maintaining competing definitions of the same contract.

### Identity, deprecation, and compatibility

Use stable IDs as the default for packaged skills. Treat display names and upstream paths as mutable metadata. When a source renames, moves, replaces, or removes a skill, update manifest references consistently and document migration impact where relevant. Do not preserve obsolete entries in the active inventory merely for historical naming continuity.

## 10. Boundaries and Non-Goals

The pack does not require a complete stack specification before useful work can start, force every task through every SDLC stage, require a persistent artifact for every action, or guarantee identical behavior across runtimes. It does not load the entire inventory into every task context or certify all upstream content as secure or legally cleared.

The pack does require explicit expectations for important results, honest uncertainty and verification reporting, authoritative package metadata, safe and traceable updates, and modular boundaries that support extension without unnecessary rewrites.

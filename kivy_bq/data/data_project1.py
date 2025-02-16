#  data_project1.py

# 2) 对应的 BQ 示例回答，支持英文/中文
#   字典键： "1","2","3",...,"12"
#   值：再用 { "en": "...", "cn": "..." } 存储两种语言答案
P1_Overall_Context = {
    """This was a project for a **Big Data course** where our group set out to build a **distributed data processing and indexing** prototype system. The primary goal was to ingest log data and support near real-time querying in a simulated environment for rapid troubleshooting and data analysis.

- We used Python and some AWS services (including Lambda, S3, and DynamoDB) for data processing and storage, and introduced Redis caching to improve query performance and system stability."""
}

P1_BQ_ANSWERS = {

    # 1
    "1": {
        "en": {
            "situation": """During my junior year of college, my professor assigned our team a challenging task: to develop a near-real-time data processing prototype within two weeks. We also had to meet multiple performance metrics, such as how quickly we could process and index one million synthetic log entries. Meanwhile, each member of the team faced the pressure of final exams, which made time management particularly difficult.""",
            "task": """My responsibility was to lead and coordinate our small team, ensuring we delivered a functional prototype within the two-week window while meeting the core performance requirements set by the professor. In other words, I needed to manage the schedule, distribute tasks effectively, and help team members balance their exam obligations and the project deadlines.""",
            "action": """**1. Confirming Core Requirements**

I first met with the professor to clarify the most important goals of the project—namely “processing speed” and “reliability,” rather than extra features. This allowed us to channel our limited time and energy into optimizing the core data pipeline instead of spreading ourselves thin on non-essential functionality.

**2. Task Breakdown & Resource Allocation**

After discussing with the professor and evaluating each teammate’s technical strengths, I divided the project into three main modules: log ingestion, indexing, and a minimal viable dashboard. One teammate had multiple exams, so I volunteered to take on additional scripting tasks to keep the overall progress on track and reduce that teammate’s workload.

**3. Frequent Communication & Rapid Iteration**

Given the two-week deadline, we adopted a high-frequency communication model. We held stand-up meetings every two days for quick progress reports and to swiftly address any issues. Additionally, I organized a more comprehensive weekly team meeting to align our overall direction, resolve potential challenges (such as AWS permissions or concurrency configuration), and ensure all subgroups stayed in sync.

**4. Mid-Project Prioritization Adjustments**

Around the midpoint of the project, we realized we couldn’t test all edge cases in the remaining time. I promptly called an emergency meeting to identify the most critical error-handling paths and high-volume scenarios. By focusing our testing efforts on these crucial areas, we avoided dissipating our resources and ensured we could complete the must-have features and testing within the deadline.""",
            "result": """Despite the tight two-week timeframe, we successfully delivered a functional prototype and improved the overall processing speed by about 40% compared to our initial tests. During the final demo, our system was able to process and index over one million synthetic logs in a very short time, earning high praise from the professor for our near-real-time performance optimizations.

Looking back, maintaining close communication and clear prioritization proved essential. By understanding each member’s exam schedule and technical strengths, we allocated tasks in a way that allowed everyone to perform at their best. Our frequent stand-ups and weekly team meetings enabled us to quickly spot issues and adjust our plans, ensuring we met all objectives within the tight timeframe. When we realized we couldn’t cover every edge case, focusing on the project’s core functionalities and tests allowed us to balance both speed and quality, ultimately delivering a high-quality result under rigorous time constraints."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": """课程的最终评审有固定交付日期，需要在有限的几周内实现从数据采集到索引查询的端到端流程。我们在实验中大约处理了几十万条模拟日志数据。""",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    # 2
    "2": {
        "en": {
            "situation": """Each teammate was responsible for different parts of the data pipeline. As we integrated our code, we found that everyone had a different way of handling errors—some used try-catch blocks, some relied on silent fails, and others just printed logs without any alerting. This lack of a unified approach made it extremely difficult to pinpoint issues, especially under high load or when logs were missing.""",
            "task": """Although my primary responsibility was to optimize the Lambda functions for faster processing, I realized that the project was at risk without a proper error-handling strategy. No one was officially assigned to unify or document these practices, but I felt it was crucial to ensure the overall reliability of our system. I decided to take the initiative to propose and implement a standardized error-handling framework, even though it was outside my original responsibility.""",
            "action": """

1. **Identify the Gap & Propose a Plan (Ownership / Customer Obsession)**

    I created a short proposal outlining how we could unify our error-handling process.

    I made sure that I detailed the benefits by explaining how consistent error logging, retry logic, and clear alerts would reduce debugging time and prevent silent failures. This could also help us develop a more reliable product.

2. **Develop a Shared Solution (Dive Deep / Bias for Action)**

    “I built a **shared utility** module for standardized error handling—covering retries, structured logs, and Slack/email alerts. (e.g., sending notifications to our Slack channel whenever an error threshold was exceeded).

    I tested this module in my own Lambda functions first, ironing out kinks and ensuring it was easy to integrate.

3. **Educate & Enable the Team (Earn Trust / Deliver Results)**

    “I organized a short workshop to show teammates how to integrate the module and demonstrate how it immediately flagged issues. Then I created a **mini wiki** with code snippets and FAQs so they could adopt it quickly in their own functions.”""",
            "result": """

“After adoption, **troubleshooting time** dropped by about 30% because e no longer had to sift through ad-hoc logs to figure out where an error occurred. 

Our pipeline became more stable in load tests, as consistent retry policies and alerts helped us catch transient failures quickly.

It also enhanced team collaboration, because everyone followed the same approach, making handoffs and code reviews smoother.

This initiative wasn’t in my original to-do list, but it ultimately **saved the project** from recurring, hard-to-diagnose errors. The professor even noted how our pipeline had fewer downtime incidents compared to similar projects."""
        },
        "cn": {
            "situation": """由于课程对错误处理没做强制要求，但我希望我们的原型具有一定的健壮性，主动设计了一个集中式的错误处理和告警机制，以防止处理流程意外终止。""",
            "task": "由于课程对错误处理没做强制要求，但我希望我们的原型具有一定的健壮性，主动设计了一个集中式的错误处理和告警机制，以防止处理流程意外终止。",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    # 3
    "3": {
        "en": {
            "situation": """During my senior year, I led a small team building a **Full-Stack Note Management System**. The goal was to enable distributed teams to **store, version, and share** large documents.

Partway through, our main stakeholder—the professor—was traveling and **couldn’t respond promptly to our questions - we wanted to clarify** some advanced features (like version control). Meanwhile, the team debated whether to **finalize backend APIs** first or build a **clickable frontend** to gather user feedback.""",
            "task": """We needed to move forward quickly to deliver a prototype for an upcoming milestone review. Without the professor’s immediate input, we had incomplete information regarding certain advanced features (e.g., file versioning logic, user permission levels), but we had to make a decision on how to start development to avoid stalling the entire team.""",
            "action": """

1. **Gather Limited Info & Weigh Options (Bias for Action / Dive Deep)**

    “I quickly reviewed the partial requirements we had,  focusing on the **core user flows:** basic note creation, file upload, and sharing. 

    I led a brief discussion with my teammates, laying out two possible approaches:

    - **Approach 1:** Build a clickable frontend prototype using a mock API so we could collect user feedback on UI/UX sooner and we avoid locking in backend details too soon.
    - **Approach 2: Implement Backend logic first** to define schemas and storage before UI.
    - We reasoned that **front-end feedback** from users would be the most critical for this milestone, because if the UI/UX was not intuitive, the rest of the system wouldn’t matter. We eventually decided to do a **lightweight frontend MVP** with fake data, while simultaneously drafting a flexible backend design in case the professor returned with new requirements.
2. **Parallel Prototyping (Invent and Simplify / Ownership)**

    “I set up a **minimal REST interface** returning dummy data so the UI team could build user flows—like note creation and file upload placeholders—without waiting for final backend logic. Meanwhile, I started an outline of our MongoDB schemas, prepared to adapt them once we got the professor’s input. This way, no one stayed idle.”

3. **Iterate & Adapt (Deliver Results / Customer Obsession)**

    “We tested the frontend prototype with classmates for early UX feedback—things like flow, layout, and basic upload steps. When the professor eventually returned, we folded his advanced feature requests (permissions, version control) into the real backend. Because we had used a mock API, integration required minimal rewrites. We delivered a user-testable MVP on time.”""",
            "result": """We **avoided blocking** the project waiting for the professor’s approval by delivering a **front-end MVP** in time for the milestone. Users could walk through the main flows (create, share, edit notes) and give feedback on usability right away.

When the professor returned, he provided insights on **version control and permissions**, which we then folded into the **real backend**. Because we had done a minimal mock setup earlier, the integration process was straightforward and **didn’t require major rewrites**.

The milestone review went well, and the professor praised our willingness to **iterate quickly** despite incomplete specs."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "4": {
        "en": {
            "situation": """During my junior year, I worked on a distributed data processing project However, we ran into a big issue: everyone had their own way of handling errors and logging, often just printing messages to the console or ignoring failures altogether. This inconsistency made it tough to troubleshoot and ensure reliability for large-scale data processing.""",
            "task": """I realized the team lacked a uniform error-handling and monitoring strategy. Wanting to improve the project’s overall stability, I decided to guide my teammates toward a standardized framework for error handling—even though this was outside my direct scope of responsibilities.""",
            "action": """

1. **Research & Preparation** 

    Spend sometime researching and teaching myself about the best practices for handling errors and logging (curiosity)

2. **Identify the Gap & Propose a Solution (Ownership / Customer Obsession)**

    “I drafted a brief plan explaining why consistent retries, structured logs, and clear alerts would help us meet our stability goals. I communicated the time-savings and reduced confusion to teammates and our professor—who effectively was our ‘customer’—to gain buy-in.”

3. **Develop & Document a Simple Utility (Dive Deep / Invent and Simplify)**

    Alongside, I wrote concise docs with examples so teammates could easily integrate it into their Lambda functions.”

4. **Hands-On Mentoring (Earn Trust / Deliver Results)**

    To ensure teammates truly understood and embraced these best practices, I **organized short workshops** demonstrating how to plug in the module, set up environment variables, and interpret logs in CloudWatch.

    I also offered **one-on-one sessions**, where I paired with teammates to migrate their existing code and taught them how to debug issues using the new logging and alerting tools.

5. **Ongoing Support & Feedback Loop (Deliver Results)**

    After the initial rollout, I continued to **check in** with teammates during stand-up meetings, gathering feedback on pain points or improvements.

    I updated the library based on their suggestions—such as adding custom tags for different error types—making the tool even more user-friendly.""",
            "result": """

“After adoption, our team **significantly cut troubleshooting time** because everyone used the same error-handling approach. Even newer members felt more at ease pushing updates, knowing they had a **robust fallback**. Ultimately, the project’s stability improved—professor load tests confirmed fewer downtime incidents."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "5": {
        "en": {
            "situation": """Midway through the project, we faced serious performance issues in DynamoDB (slow queries, occasional timeouts). There was no official directive or time to deeply research solutions.
- Redis was unfamiliar to our team, so introducing it might complicate the pipeline. However, our logs were hammering DynamoDB, indicating a caching solution could really help.""",
            "task": """I needed to decide quickly whether to adopt Redis caching without a thorough feasibility study (due to tight timelines).""",
            "action": """1. **Quick Investigation**: I skimmed Redis documentation and community examples to understand caching benefits and limitations.
2. **Prototype in Test Environment**: I set up a minimal Redis instance, tested a subset of data, and measured cache hit rates vs. DynamoDB read frequency.
3. **Proceed Without Formal Approval**: Despite limited info, I integrated Redis into our core pipeline, giving us a “Plan B” to revert if it failed.
4. **Mitigation Strategy**: I created a rollback script that would disable Redis if we saw no improvement or negative side effects.""",
            "result": """- **Throughput Increased**: Once Redis was in place, our query times dropped by ~20%, further boosting overall performance.
- **Positive Team Feedback**: My bold decision led to a timely solution and was well-received.
- **Lesson**: Taking a **calculated risk** can be beneficial when deadlines are pressing, as long as you have a fallback plan."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "6": {
        "en": {
            "situation": """- I promised to implement a custom CloudWatch-based monitoring and alert system for Redis usage within a one-week sprint.
- Underestimated complexity: self-defined CloudWatch metrics turned out to be more intricate than expected, and I also had to tackle other coursework tasks.""",
            "task": """I aimed to deliver the full monitoring and alerting suite within a single sprint, but progress stalled after a few days because of unforeseen challenges.""",
            "action": """1. **Early Communication**: I informed my teammates that I was behind schedule and shared the technical hurdles (configuring custom metrics, debugging permission issues).
2. **Adjust Scope**: We agreed I’d complete only basic Redis health checks (availability/latency) this sprint, pushing advanced alerts to the next iteration.
3. **Seek Help**: I paired with a classmate familiar with AWS to quickly learn how to create robust CloudWatch alarms for memory usage and key eviction rates.""",
            "result": """- **Partial Delivery**: By the end of that sprint, only the essential metrics were in place.
- **No Major Project Delay**: Because we communicated early and scaled back scope, the main pipeline stayed on track.
- **Lesson**: I learned to be more realistic with time estimates when working with new technology. Overpromising can lead to late re-scoping."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "7": {
        "en": {
            "situation": """- We only had a limited sample of historical log data (tens of thousands of entries), but the final target might be hundreds of thousands or even more.
- Waiting for more “real” data could stall progress, while starting immediately might force redesign if the logs turned out very different from our assumptions.""",
            "task": """Decide whether to gather more real-world data or move forward with an early prototype. The course deadline was tight.""",
            "action": """1. **MVP Approach**: I chose to build the core pipeline using the logs we already had plus synthetic logs that mimicked potential future patterns.
2. **Flexible Data Design**: I made DynamoDB’s partition key generic enough to accommodate changes if the log schema evolved.
3. **Iterative Testing**: We rolled out a minimal “version one,” did quick performance tests, then incorporated any new findings as more log samples became available.""",
            "result": """- **Prototype Up and Running**: We didn’t get stuck waiting, so we delivered an initial end-to-end solution ahead of schedule.
- **Adaptable Architecture**: When newer logs arrived, we made only minor tweaks to the schema—no major rewrite needed.
- **Lesson**: Sometimes starting with limited data and iterating is better than waiting indefinitely for perfect information."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "8": {
        "en": {
            "situation": """- Early on, I believed that simply increasing Lambda concurrency limits would speed up processing. I ramped concurrency too high, assuming “more parallelism = better.”
- The result was severe “hot partition” issues in DynamoDB, causing write throttling and spiking AWS bills.""",
            "task": """I had to correct my oversight quickly, without losing the benefit of parallel processing entirely.""",
            "action": """1. **Identify the Root Cause**: Spotted DynamoDB alarms, abnormally high AWS costs, and slow writes, revealing a partition hot-spot problem.
2. **Acknowledge Mistake**: I informed the team and admitted I’d overlooked DynamoDB’s partition capacity constraints.
3. **Implement Fix**:
    - Reduced Lambda concurrency to a moderate level.
    - Added a simple “batch write” logic and refined DynamoDB partition-key strategy to distribute writes more evenly.""",
            "result": """- **System Stabilized**: Write throttling ceased, costs normalized, and throughput improved.
- **Lesson**: Unlimited concurrency can backfire if the downstream service (DynamoDB) isn’t scaled or partitioned correctly."""
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "9": {
        "en": {
            "situation": """""",
            "task": """""",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "10": {
        "en": {
            "situation": """""",
            "task": """""",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "11": {
        "en": {
            "situation": """""",
            "task": "我负责管理进度...",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "12": {
        "en": {
            "situation": """""",
            "task": "我负责管理进度...",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": "我负责管理进度...",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    }
}

# 5) 针对各 Project，各 LP 对应的 Follow-up 问题 & 答案
#   每个项目的 LP 不变，但每个项目出现的跟进问题 / 答案不一样
Project1_LP_FOLLOWUP_QUESTIONS = {
    1: "P1 Follow-up Q: 面对客户需求，你如何优先处理？",
    2: "P1 Follow-up Q: 你如何在团队中推广主人翁精神？",
    # 此处可继续补充 3 ~ 16
}
Project1_LP_FOLLOWUP_ANSWER = {
    1: "P1 Follow-up A: 我会先评估业务价值与紧急程度，逐步迭代……",
    2: "P1 Follow-up A: 我会主动承担责任，也鼓励队友独立解决问题……",
    # … 3 ~ 16
}
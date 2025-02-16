#  data_project1.py

# 2) 对应的 BQ 示例回答，支持英文/中文
#   字典键： "1","2","3",...,"12"
#   值：再用 { "en": "...", "cn": "..." } 存储两种语言答案
P1_Overall_Context = {
    """This was a project for a **Big Data course** where our group set out to build a **distributed data processing and indexing** prototype system. The primary goal was to ingest log data and support near real-time querying in a simulated environment for rapid troubleshooting and data analysis.

- We used Python and some AWS services (including Lambda, S3, and DynamoDB) for data processing and storage, and introduced Redis caching to improve query performance and system stability."""
}


P1_BQ_ANSWERS = {
    "1":  {
        "en": {
            "situation": """The course had a set due date for final presentations, meaning we had only a few weeks to implement an end-to-end pipeline for data ingestion, processing, and indexing. We worked with tens of thousands of sample log entries in our test environment.""",
            "task": """课程的最终评审有固定交付日期，需要在有限的几周内实现从数据采集到索引查询的端到端流程。我们在实验中大约处理了几十万条模拟日志数据。""",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": "我们只有两周时间完成一个原型...",
            "task": """课程的最终评审有固定交付日期，需要在有限的几周内实现从数据采集到索引查询的端到端流程。我们在实验中大约处理了几十万条模拟日志数据。""",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },


    "2":   {
        "en": {
            "situation": """Although the course requirements didn’t mandate error handling or fault tolerance, I took the initiative to design a simple centralized error-handling mechanism, aiming for better stability in our distributed setup.""",
            "task": """Although the course requirements didn’t mandate error handling or fault tolerance, I took the initiative to design a simple centralized error-handling mechanism, aiming for better stability in our distributed setup.""",
            "action": "- Step1...\n- Step2...\n- Step3...",
            "result": "We completed on time and increased performance by 40%..."
        },
        "cn": {
            "situation": """由于课程对错误处理没做强制要求，但我希望我们的原型具有一定的健壮性，主动设计了一个集中式的错误处理和告警机制，以防止处理流程意外终止。""",
            "task": "由于课程对错误处理没做强制要求，但我希望我们的原型具有一定的健壮性，主动设计了一个集中式的错误处理和告警机制，以防止处理流程意外终止。",
            "action": "- 第一步...\n- 第二步...\n- 第三步...",
            "result": "我们按时完成，性能提高了40%..."
        }
    },

    "3":   {
        "en": {
            "situation": """One member of the team was new to distributed systems, so I conducted knowledge-sharing sessions to accelerate their understanding of distributed processing and indexing fundamentals.""",
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

    "4":   {
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

    "5":   {
        "en": {
            "situation": """- Midway through the project, we faced serious performance issues in DynamoDB (slow queries, occasional timeouts). There was no official directive or time to deeply research solutions.
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

    "6":   {
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

    "7":   {
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

    "8":   {
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

    "9":   {
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

    "10":  {
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

    "11":  {
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

    "12":  {
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
    1:  "P1 Follow-up Q: 面对客户需求，你如何优先处理？",
    2:  "P1 Follow-up Q: 你如何在团队中推广主人翁精神？",
    # 此处可继续补充 3 ~ 16
}
Project1_LP_FOLLOWUP_ANSWER = {
    1:  "P1 Follow-up A: 我会先评估业务价值与紧急程度，逐步迭代……",
    2:  "P1 Follow-up A: 我会主动承担责任，也鼓励队友独立解决问题……",
    # … 3 ~ 16
}
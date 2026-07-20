Parse the Apache-style access log at /app/access.log and write a JSON summary
report to /app/report.json.

Success criteria:
1. /app/report.json exists and is valid JSON.
2. The report contains integer key "total_requests" equal to the number of
   non-empty log lines in /app/access.log.
3. The report contains integer key "unique_ips" equal to the number of distinct
   client IP addresses (first whitespace-separated field of each line).
4. The report contains string key "top_path" equal to the request path that
   appears most often in the quoted request section of each line
   (e.g. GET /index.html HTTP/1.1 → path /index.html). If there is a tie,
   use the path that appears first in the log among the tied paths.
5. Do not modify /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.

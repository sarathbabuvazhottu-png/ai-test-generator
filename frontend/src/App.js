import { useState } from "react";

function App() {
  const [code, setCode] = useState("");
  const [style, setStyle] = useState("basic");
  const [tests, setTests] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);
  const [results, setResults] = useState(null);
  const [running, setRunning] = useState(false);

  const generateTests = async () => {
    if (!code.trim()) {
      setError("Please paste your Python code first!");
      return;
    }

    setLoading(true);
    setError("");
    setTests("");
    setResults(null);

    try {
      const response = await fetch(
        "http://localhost:5000/generate",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ code, style }),
        }
      );

      const data = await response.json();

      if (data.success) {
        setTests(data.tests);
      } else {
        setError(data.error || "Something went wrong!");
      }
    } catch (err) {
      setError(
        "Cannot connect to server! Make sure Flask is running!"
      );
    }

    setLoading(false);
  };

  const runTests = async () => {
    if (!tests) {
      setError("Generate tests first!");
      return;
    }

    setRunning(true);
    setError("");

    try {
      const response = await fetch(
        "http://localhost:5000/run-tests",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ tests, style }),
        }
      );

      const data = await response.json();

      if (data.success) {
        setResults(data.results);
      } else {
        setError(data.error || "Could not run tests!");
      }
    } catch (err) {
      setError("Cannot connect to server!");
    }

    setRunning(false);
  };

  const copyTests = () => {
    navigator.clipboard.writeText(tests);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const downloadTests = () => {
    const blob = new Blob([tests], {
      type: "text/plain",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `test_${style}_generated.py`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const countTests = (testCode) => {
    const matches = testCode.match(/def test_/g);
    return matches ? matches.length : 0;
  };

  return (
    <div style={styles.container}>

      {/* Header */}
      <div style={styles.header}>
        <h1 style={styles.title}>
          🤖 AI Test Generator
        </h1>
        <p style={styles.subtitle}>
          Paste your Python code and get
          tests generated automatically!
        </p>
      </div>

      {/* Main Content */}
      <div style={styles.main}>

        {/* Left Side — Input */}
        <div style={styles.card}>
          <h2 style={styles.cardTitle}>
            📝 Your Python Code
          </h2>

          <textarea
            style={styles.textarea}
            placeholder="Paste your Python code here...

Example:
def add_numbers(a, b):
    return a + b"
            value={code}
            onChange={(e) => setCode(e.target.value)}
          />

          <h3 style={styles.label}>
            🎯 Select Prompt Style:
          </h3>

          <div style={styles.styleButtons}>
            {["basic", "detailed", "expert"].map((s) => (
              <button
                key={s}
                style={{
                  ...styles.styleBtn,
                  ...(style === s
                    ? styles.styleBtnActive
                    : {}),
                }}
                onClick={() => setStyle(s)}
              >
                {s === "basic" && "⚡ Basic"}
                {s === "detailed" && "📋 Detailed"}
                {s === "expert" && "🏆 Expert"}
              </button>
            ))}
          </div>

          <p style={styles.styleDesc}>
            {style === "basic" &&
              "⚡ Basic — Simple tests, fast results!"}
            {style === "detailed" &&
              "📋 Detailed — Normal, edge case and error tests!"}
            {style === "expert" &&
              "🏆 Expert — ALL possible tests like a senior developer!"}
          </p>

          <button
            style={{
              ...styles.generateBtn,
              ...(loading
                ? styles.btnDisabled
                : {}),
            }}
            onClick={generateTests}
            disabled={loading}
          >
            {loading
              ? "⏳ Generating Tests..."
              : "🚀 Generate Tests!"}
          </button>

          {error && (
            <div style={styles.error}>
              ❌ {error}
            </div>
          )}
        </div>

        {/* Right Side — Output */}
        <div style={styles.card}>

          {/* Output Header */}
          <div style={styles.outputHeader}>
            <h2 style={styles.cardTitle}>
              ✅ Generated Tests
            </h2>
            {tests && (
              <div style={styles.btnGroup}>
                <button
                  style={styles.copyBtn}
                  onClick={copyTests}
                >
                  {copied ? "✅ Copied!" : "📋 Copy"}
                </button>
                <button
                  style={styles.downloadBtn}
                  onClick={downloadTests}
                >
                  ⬇️ Download
                </button>
              </div>
            )}
          </div>

          {/* Test Count Badge */}
          {tests && (
            <div style={styles.badge}>
              🧪 {countTests(tests)} tests generated!
            </div>
          )}

          {/* Run Tests Button */}
          {tests && (
            <button
              style={{
                ...styles.runBtn,
                ...(running ? styles.btnDisabled : {}),
              }}
              onClick={runTests}
              disabled={running}
            >
              {running
                ? "⏳ Running Tests..."
                : "▶️ Run Tests and See Results!"}
            </button>
          )}

          {/* Results Table */}
          {results && (
            <div style={styles.resultsBox}>
              <h3 style={styles.resultsTitle}>
                📊 Test Results
              </h3>
              <table style={styles.table}>
                <thead>
                  <tr>
                    <th style={styles.th}>Metric</th>
                    <th style={styles.th}>Result</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      🧪 Total Tests
                    </td>
                    <td style={styles.tdBold}>
                      {results.total}
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      ✅ Passed
                    </td>
                    <td style={{
                      ...styles.tdBold,
                      color: "#22c55e"
                    }}>
                      {results.passed}
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      ❌ Failed
                    </td>
                    <td style={{
                      ...styles.tdBold,
                      color: results.failed > 0
                        ? "#ef4444"
                        : "#22c55e"
                    }}>
                      {results.failed}
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      🎯 Pass Rate
                    </td>
                    {/* Pytest Raw Output */}
                  {results.output && (
                    <div style={{marginTop: "15px"}}>
                      <h4 style={{
                        color: "#333",
                        margin: "0 0 8px 0"
                      }}>
                        📋 Pytest Output:
                      </h4>
                      <pre style={{
                        background: "#1e1e1e",
                        color: "#d4d4d4",
                        padding: "12px",
                        borderRadius: "8px",
                        fontSize: "0.75rem",
                        overflow: "auto",
                        maxHeight: "200px",
                        whiteSpace: "pre-wrap"
                      }}>
                        {results.output}
                      </pre>
                    </div>
                  )}

                  {/* Pass Rate Bar */}
                    <td style={{
                      ...styles.tdBold,
                      color: results.pass_rate === "100.0%"
                        ? "#22c55e"
                        : "#f59e0b"
                    }}>
                      {results.pass_rate}
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      📊 Coverage
                    </td>
                    <td style={{
                      ...styles.tdBold,
                      color: "#667eea"
                    }}>
                      {results.coverage}
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      🤖 AI Model
                    </td>
                    <td style={styles.tdBold}>
                      Claude Sonnet
                    </td>
                  </tr>
                  <tr style={styles.tr}>
                    <td style={styles.td}>
                      🎨 Prompt Style
                    </td>
                    <td style={styles.tdBold}>
                      {style}
                    </td>
                  </tr>
                </tbody>
              </table>

              {/* Pass Rate Bar */}
              <div style={styles.barContainer}>
                <div style={styles.barLabel}>
                  Pass Rate
                </div>
                <div style={styles.barBg}>
                  <div style={{
                    ...styles.barFill,
                    width: results.pass_rate,
                    background: results.pass_rate === "100.0%"
                      ? "#22c55e"
                      : "#f59e0b"
                  }}/>
                </div>
                <div style={styles.barValue}>
                  {results.pass_rate}
                </div>
              </div>
            </div>
          )}

          {/* Empty State */}
          {!tests && !loading && (
            <div style={styles.emptyState}>
              <p>🤖 Tests will appear here!</p>
              <p>Paste your code and
                click Generate!</p>
            </div>
          )}

          {/* Loading State */}
          {loading && (
            <div style={styles.emptyState}>
              <p>⏳ Claude AI is writing
                your tests...</p>
              <p>This takes about
                10-20 seconds!</p>
            </div>
          )}

          {/* Tests Output */}
          {tests && (
            <pre style={styles.output}>
              {tests}
            </pre>
          )}
        </div>
      </div>

      {/* Footer */}
      <div style={styles.footer}>
        <p>
          Built for Developers •
          Python • React 
        </p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    background:
      "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    fontFamily: "Arial, sans-serif",
    padding: "20px",
  },
  header: {
    textAlign: "center",
    padding: "30px 0 20px 0",
  },
  title: {
    color: "white",
    fontSize: "2.5rem",
    margin: "0 0 10px 0",
  },
  subtitle: {
    color: "rgba(255,255,255,0.85)",
    fontSize: "1.1rem",
    margin: 0,
  },
  main: {
    display: "flex",
    gap: "20px",
    maxWidth: "1200px",
    margin: "0 auto",
    flexWrap: "wrap",
  },
  card: {
    background: "white",
    borderRadius: "16px",
    padding: "25px",
    flex: 1,
    minWidth: "300px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.2)",
  },
  cardTitle: {
    margin: "0 0 15px 0",
    color: "#333",
    fontSize: "1.3rem",
  },
  textarea: {
    width: "100%",
    height: "260px",
    padding: "12px",
    borderRadius: "8px",
    border: "2px solid #e0e0e0",
    fontFamily: "monospace",
    fontSize: "0.9rem",
    resize: "vertical",
    boxSizing: "border-box",
    outline: "none",
  },
  label: {
    margin: "15px 0 10px 0",
    color: "#555",
    fontSize: "1rem",
  },
  styleButtons: {
    display: "flex",
    gap: "10px",
    marginBottom: "10px",
  },
  styleBtn: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px",
    border: "2px solid #e0e0e0",
    background: "white",
    cursor: "pointer",
    fontSize: "0.9rem",
    fontWeight: "bold",
    color: "#666",
  },
  styleBtnActive: {
    border: "2px solid #667eea",
    background: "#667eea",
    color: "white",
  },
  styleDesc: {
    color: "#888",
    fontSize: "0.85rem",
    margin: "5px 0 15px 0",
  },
  generateBtn: {
    width: "100%",
    padding: "15px",
    borderRadius: "10px",
    border: "none",
    background:
      "linear-gradient(135deg, #667eea, #764ba2)",
    color: "white",
    fontSize: "1.1rem",
    fontWeight: "bold",
    cursor: "pointer",
  },
  runBtn: {
    width: "100%",
    padding: "12px",
    borderRadius: "10px",
    border: "none",
    background:
      "linear-gradient(135deg, #22c55e, #16a34a)",
    color: "white",
    fontSize: "1rem",
    fontWeight: "bold",
    cursor: "pointer",
    marginBottom: "15px",
  },
  btnDisabled: {
    opacity: 0.7,
    cursor: "not-allowed",
  },
  error: {
    marginTop: "10px",
    padding: "10px",
    borderRadius: "8px",
    background: "#fff0f0",
    color: "#cc0000",
    fontSize: "0.9rem",
  },
  outputHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "10px",
  },
  btnGroup: {
    display: "flex",
    gap: "8px",
  },
  copyBtn: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "none",
    background: "#667eea",
    color: "white",
    cursor: "pointer",
    fontWeight: "bold",
    fontSize: "0.85rem",
  },
  downloadBtn: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "none",
    background: "#764ba2",
    color: "white",
    cursor: "pointer",
    fontWeight: "bold",
    fontSize: "0.85rem",
  },
  badge: {
    display: "inline-block",
    background: "#f0f4ff",
    color: "#667eea",
    padding: "6px 14px",
    borderRadius: "20px",
    fontSize: "0.9rem",
    fontWeight: "bold",
    marginBottom: "12px",
  },
  resultsBox: {
    background: "#f8faff",
    borderRadius: "12px",
    padding: "15px",
    marginBottom: "15px",
    border: "1px solid #e0e8ff",
  },
  resultsTitle: {
    margin: "0 0 12px 0",
    color: "#333",
    fontSize: "1.1rem",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginBottom: "15px",
  },
  th: {
    background: "#667eea",
    color: "white",
    padding: "10px",
    textAlign: "left",
    fontSize: "0.9rem",
  },
  tr: {
    borderBottom: "1px solid #e0e0e0",
  },
  td: {
    padding: "10px",
    color: "#555",
    fontSize: "0.9rem",
  },
  tdBold: {
    padding: "10px",
    fontWeight: "bold",
    fontSize: "0.95rem",
    color: "#333",
  },
  barContainer: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
  },
  barLabel: {
    fontSize: "0.85rem",
    color: "#666",
    minWidth: "70px",
  },
  barBg: {
    flex: 1,
    background: "#e0e0e0",
    borderRadius: "10px",
    height: "12px",
    overflow: "hidden",
  },
  barFill: {
    height: "100%",
    borderRadius: "10px",
    transition: "width 0.5s ease",
  },
  barValue: {
    fontSize: "0.85rem",
    fontWeight: "bold",
    color: "#333",
    minWidth: "50px",
  },
  emptyState: {
    textAlign: "center",
    color: "#aaa",
    padding: "40px 20px",
    lineHeight: "2",
  },
  output: {
    background: "#1e1e1e",
    color: "#d4d4d4",
    padding: "15px",
    borderRadius: "8px",
    fontSize: "0.8rem",
    overflow: "auto",
    maxHeight: "300px",
    whiteSpace: "pre-wrap",
    wordBreak: "break-word",
  },
  footer: {
    textAlign: "center",
    color: "rgba(255,255,255,0.7)",
    padding: "20px",
    fontSize: "0.9rem",
  },
};

export default App;
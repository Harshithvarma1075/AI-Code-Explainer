import { useState } from "react";

import "./MainLayout.css";

import CodeEditor from "../CodeEditor/CodeEditor";
import ResponsePanel from "../ResponsePanel/ResponsePanel";

function MainLayout() {
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);

  return (
    <section className="main-layout">
      <div className="left-panel">
        <div className="panel-header">
          <h2>Code Editor</h2>
        </div>

        <CodeEditor
          onResponse={setResponse}
          loading={loading}
          setLoading={setLoading}
          sessionId={sessionId}
          onSessionId={setSessionId}
          onResetConversation={() => setSessionId(null)}
        />
      </div>

      <div className="right-panel">
        <div className="panel-header">
          <h2>AI Response</h2>
        </div>

        <ResponsePanel
          response={response}
          loading={loading}
        />
      </div>
    </section>
  );
}

export default MainLayout;

import { useState } from "react";
import { CopyToClipboard } from "react-copy-to-clipboard";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";

import {
  oneLight,
  oneDark,
} from "react-syntax-highlighter/dist/esm/styles/prism";

import { FaCopy, FaCheck } from "react-icons/fa";

import { useTheme } from "../../context/ThemeContext";

import "./MarkdownCodeBlock.css";

function MarkdownCodeBlock({
  language,
  code,
}) {
  const [copied, setCopied] = useState(false);

  const { theme } = useTheme();

  const handleCopy = () => {
    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  return (
    <div className="markdown-code-block">

      <div className="code-header">

        <span className="code-language">
          {language || "text"}
        </span>

        <CopyToClipboard
          text={code}
          onCopy={handleCopy}
        >
          <button className="copy-btn">

            {copied ? (
              <>
                <FaCheck />
                Copied
              </>
            ) : (
              <>
                <FaCopy />
                Copy
              </>
            )}

          </button>
        </CopyToClipboard>

      </div>

      <SyntaxHighlighter
        language={language}
        style={theme === "dark" ? oneDark : oneLight}
        customStyle={{
          margin: 0,
          borderRadius: "0 0 10px 10px",
          fontSize: "14px",
        }}
      >
        {code}
      </SyntaxHighlighter>

    </div>
  );
}

export default MarkdownCodeBlock;
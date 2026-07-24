import "./DownloadButton.css";
import { downloadMarkdown } from "../../utils/downloadUtils";
import { showSuccess } from "../../utils/toastUtils";

function DownloadButton({ content }) {
  const handleDownload = () => {
  if (!content) return;

  downloadMarkdown(content);
  showSuccess("AI analysis downloaded successfully!");
};

  return (
    <button
      className="download-btn"
      onClick={handleDownload}
      disabled={!content}
    >
      Download Markdown
    </button>
  );
}

export default DownloadButton;
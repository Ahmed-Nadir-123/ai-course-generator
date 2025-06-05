import React, { useState } from 'react';
import './styles/CourseDisplay.scss';
import { generatePPT, generatePDF, generateLabSheet, downloadFile } from './api';

function parseCourseContent(course) {
  // Try to parse course content if it's a stringified JSON, else fallback
  if (!course) return null;
  if (typeof course === 'string') {
    try {
      return JSON.parse(course);
    } catch {
      return { raw: course };
    }
  }
  return course;
}

function CourseDisplay({ course }) {
  const [expanded, setExpanded] = useState(false);
  const [downloading, setDownloading] = useState('');
  const [error, setError] = useState('');
  const parsed = parseCourseContent(course);

  const handleDownload = async (type) => {
    setDownloading(type);
    setError('');
    try {
      let res;
      if (type === 'ppt') res = await generatePPT(course);
      else if (type === 'pdf') res = await generatePDF(course);
      else if (type === 'lab') res = await generateLabSheet(course);
      const fileId = res.data.file_id;
      const fileRes = await downloadFile(fileId);
      const url = window.URL.createObjectURL(new Blob([fileRes.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', fileId);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (e) {
      setError('Download failed.');
    }
    setDownloading('');
  };

  if (!course) return null;
  return (
    <div className="course-display">
      <button onClick={() => setExpanded(e => !e)}>
        {expanded ? 'Hide Course Details' : 'Show Course Details'}
      </button>
      {expanded && (
        <>
          <div className="download-buttons">
            <button onClick={() => handleDownload('ppt')} disabled={!!downloading}>
              {downloading === 'ppt' ? 'Downloading...' : 'Download PowerPoint'}
            </button>
            <button onClick={() => handleDownload('pdf')} disabled={!!downloading}>
              {downloading === 'pdf' ? 'Downloading...' : 'Download PDF'}
            </button>
            <button onClick={() => handleDownload('lab')} disabled={!!downloading}>
              {downloading === 'lab' ? 'Downloading...' : 'Download Lab Sheet'}
            </button>
          </div>
          {error && <div className="error">{error}</div>}
          <div className="course-content">
            {parsed && parsed.raw ? (
              <pre>{parsed.raw}</pre>
            ) : (
              <>
                {parsed && parsed['COURSE OVERVIEW'] && (
                  <section>
                    <h2>Course Overview</h2>
                    <pre>{JSON.stringify(parsed['COURSE OVERVIEW'], null, 2)}</pre>
                  </section>
                )}
                {parsed && parsed['MODULES'] && (
                  <section>
                    <h2>Modules</h2>
                    <pre>{JSON.stringify(parsed['MODULES'], null, 2)}</pre>
                  </section>
                )}
                {/* Add more structured sections as needed */}
              </>
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default CourseDisplay;

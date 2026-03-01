<div align="center">

# ATS Resume Builder
**Created by Sarmad Nadeem**

[![React](https://img.shields.io/badge/React-18.2.0-blue?style=for-the-badge&logo=react)](https://react.dev)
[![Client Side](https://img.shields.io/badge/100%25-Client_Side-green?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/API)
[![Privacy First](https://img.shields.io/badge/Privacy-Focused-purple?style=for-the-badge)](https://github.com)

A professional, 100% client-side privacy-focused ATS (Applicant Tracking System) Resume Builder. Designed by **Sarmad Nadeem** to bypass complex backend document generation by rendering pixel-perfect PDF and `.docx` exports right in your browser.

</div>

<br/>

## 🚀 The Value Proposition

This application leverages modern web technologies to process, structure, and export resumes locally.
- **Privacy First**: No server-side rendering, no database storage, and no APIs are required to generate your documents. Your data stays entirely in your browser.
- **Parser Perfect**: The UI and exported documents use a hyper-optimized, single-column layout strictly built to ensure 100% compatibility with automated HR Applicant Tracking Systems.

## ⚡ Core Features

* **ATS Optimization**: No complex tables, no distracting icons, and a strict, professional single-column hierarchy ensuring parsing engines can easily extract your work history and skills.
* **Live, Synchronized Preview**: Type in the form on the left, and watch the resume render instantaneously on the right. Form data and HTML visualization are locked in real-time synchronization.
* **Hybrid Exports**: Direct, high-fidelity browser generation.
  * *PDFs* are captured and scaled accurately using `html2canvas` and `jsPDF`.
  * *.docx* Files are built natively in XML and packaged via `JSZip`, allowing instant edits in MS Word.
* **Precision Tools**: Includes custom Python utilities (`bump_font.py`, `bump_font_small.py`) capable of parsing document CSS and XML logic for pixel-perfect font scaling and half-point adjustments to guarantee single-page rendering.

## 🛠️ Tech Stack & Dependencies

Built relying solely on vanilla standard tooling to ensure performance and portability:

* **React 18** (via untranspiled Babel browser usage)
* **jsPDF** & **html2canvas** (Client-side PDF rendering engine)
* **JSZip** (On-the-fly MS Word XML bundling and zipping)
* **Vanilla CSS / HTML5**

## 💡 Pro UI / UX Philosophy

The builder integrates high-end aesthetic feedback during generation:
* **Glassmorphism States**: Beautiful blur-filtered loading overlays ensuring a premium feel when transitioning between DOM states.
* **Micro-Interactions**: Features CSS-driven "Pop and Pulse" button logic and real-time generation feedback loops utilizing pure React State and Keyframe animations.

---

<div align="center">
  <p><b>Developed and maintained by Sarmad Nadeem.</b></p>
</div>

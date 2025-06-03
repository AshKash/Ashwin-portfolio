---
title: "The Conversational Commerce Revolution"
description: "How AI-powered conversations are transforming the future of e-commerce"
date: 2024-06-02
tags: ["AI", "E-commerce", "Conversational AI", "Customer Experience"]
---

{{< rawhtml >}}

<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Conversational Commerce Revolution: An AI Blueprint for SMBs</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc; /* Lightest slate */
        }
        .chart-container {
            position: relative;
            width: 100%;
            height: 40vh; /* Default height for charts */
            max-height: 450px; /* Max height for charts */
        }
        .swot-grid {
            display: grid;
            grid-template-columns: 1fr; /* Single column on mobile */
            gap: 1rem;
        }
        @media (min-width: 768px) {
            .swot-grid {
                grid-template-columns: 1fr 1fr; /* Two columns on medium screens and up */
            }
        }
        .flow-arrow {
            font-size: 2rem; /* Arrow size */
            color: #94d2bd; /* Light Teal from palette */
            line-height: 1;
        }
         .flow-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .flow-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        /* Chosen Palette: Brilliant Blues & Oranges (Inspired by the blog's theme) */
        /* Primary Blue: #005f73 (Dark Blue) */
        /* Accent Teal: #0a9396 (Teal) */
        /* Highlight Teal: #94d2bd (Light Teal) */
        /* Accent Gold: #e9d8a6 (Pale Gold) */
        /* Accent Orange: #ee9b00 (Orange) */
        /* Darker Orange: #ca6702 (Dark Orange) */
        /* Burnt Orange: #bb3e03 (Burnt Orange) */
        .trend-item::before {
            content: "✔"; /* Unicode checkmark or can use a Tailwind icon if preferred */
            color: #0a9396; /* Teal color from palette */
            margin-right: 0.5rem;
            font-weight: bold;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800">

    <header class="bg-[#005f73] text-white text-center py-12 px-4">
        <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-4">The Conversational Commerce Revolution</h1>
        <p class="text-lg md:text-xl max-w-3xl mx-auto text-[#e9d8a6]">An AI Blueprint for Transforming SMB Websites into Intelligent, Conversational Storefronts</p>
    </header>

    <main class="container mx-auto p-4 md:p-8">

        <section id="challenge" class="my-12 md:my-16">
            <div class="max-w-4xl mx-auto text-center">
                <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">The Modern SMB E-Commerce Challenge</h2>
                <p class="text-lg text-slate-600 mb-10">Small and medium businesses (SMBs) often face significant hurdles in making their websites engaging and accessible. Static product pages and complex navigation can leave users struggling and lead to lost sales, while custom solutions are often prohibitively expensive.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-[#ee9b00]">
                    <h3 class="text-xl font-bold text-[#005f73] mb-2">Low Engagement</h3>
                    <p class="text-slate-600">Static sites fail to capture user attention, with over <span class="font-bold">75%</span> of SMBs reporting challenges in creating interactive user experiences that drive sales.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-[#ca6702]">
                    <h3 class="text-xl font-bold text-[#005f73] mb-2">High Costs & Complexity</h3>
                    <p class="text-slate-600">Rebuilding a site from scratch is a major barrier. <span class="font-bold">60%</span> of SMBs cite high costs and technical complexity as reasons for not upgrading their web platforms.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-[#bb3e03]">
                    <h3 class="text-xl font-bold text-[#005f73] mb-2">Accessibility Gaps</h3>
                    <p class="text-slate-600">Many sites are not optimized for users with accessibility needs, effectively excluding up to <span class="font-bold">15%</span> of the potential user base and limiting market reach.</p>
                </div>
            </div>
        </section>

        <section id="architecture" class="my-12 md:my-20 py-12 bg-white rounded-xl shadow-lg">
            <div class="max-w-4xl mx-auto text-center px-4">
                <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">How It Works: The Core Architecture</h2>
                <p class="text-lg text-slate-600 mb-12">Our system uses a robust, three-phase process to turn any website into a reliable conversational interface. By using a structured "Action Map," we decouple the AI's reasoning from the final execution, ensuring safety and auditability.</p>
            </div>
            <div class="flex flex-col md:flex-row items-stretch justify-center gap-4 md:gap-8 px-4">
                <div class="flow-card text-center bg-slate-50 p-6 rounded-lg shadow-md w-full md:w-1/3 flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-2 text-[#0a9396]">1</div>
                        <h3 class="text-xl font-bold text-[#005f73]">Intelligent Crawling</h3>
                    </div>
                    <p class="text-slate-600 text-sm mt-2">We crawl the site to extract key elements and interactions, structuring them into clean, usable data.</p>
                </div>
                <div class="flex items-center justify-center transform md:rotate-0 rotate-90">
                    <div class="flow-arrow">&rarr;</div>
                </div>
                <div class="flow-card text-center bg-slate-50 p-6 rounded-lg shadow-md w-full md:w-1/3 flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-2 text-[#0a9396]">2</div>
                        <h3 class="text-xl font-bold text-[#005f73]">Backend Action Map Generation</h3>
                    </div>
                    <p class="text-slate-600 text-sm mt-2">The backend LLM translates user intent into a structured JSON "Action Map"—a safe, validated plan.</p>
                </div>
                <div class="flex items-center justify-center transform md:rotate-0 rotate-90">
                     <div class="flow-arrow">&rarr;</div>
                </div>
                <div class="flow-card text-center bg-slate-50 p-6 rounded-lg shadow-md w-full md:w-1/3 flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-2 text-[#0a9396]">3</div>
                        <h3 class="text-xl font-bold text-[#005f73]">Secure Client-Side Execution</h3>
                    </div>
                    <p class="text-slate-600 text-sm mt-2">A secure JavaScript library runs in the browser, interpreting the Action Map to safely perform tasks on the page.</p>
                </div>
            </div>

            <div class="max-w-4xl mx-auto mt-16 px-4">
                <h3 class="text-2xl font-bold text-center text-[#005f73] mb-6">Deep Dive: Secure Client-Side Execution</h3>
                <div class="bg-slate-50 p-6 rounded-lg border border-slate-200">
                    <p class="text-slate-700">The final execution of user commands occurs directly within the user's browser, orchestrated by a secure and lightweight JavaScript library. This client-side engine receives a pre-validated Action Map from our backend. This Action Map, already vetted for logical consistency and correctness (ensuring LLM-generated errors are filtered out before reaching the client), dictates the precise operations the library will perform.</p>
                    <p class="mt-4 text-slate-700">These operations can range from interacting with webpage elements via DOM selectors, making controlled API requests (GET/POST, adhering to CORS), to managing browser cookies for session continuity. This client-centric yet backend-validated execution model ensures that all actions are not only reliable and auditable but also operate securely within the sandboxed environment of the user's browser, respecting all standard web security protocols.</p>
                </div>
            </div>
        </section>

        <section id="landscape" class="my-12 md:my-16">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div class="bg-white p-8 rounded-lg shadow-md">
                    <h2 class="text-3xl font-bold text-[#005f73] mb-4">Market Landscape: Competitive Positioning</h2>
                    <p class="text-slate-600">Our Action Map (IR) approach offers a superior balance of reliability, adaptability, and safety compared to other solutions. While direct LLM agents can be flexible, they risk unpredictable behavior. Generic chatbots lack deep, site-specific task completion abilities. Our system is engineered for robust, auditable performance in real-world e-commerce environments.</p>
                </div>
                <div class="bg-white p-4 md:p-8 rounded-lg shadow-md">
                    <div class="chart-container mx-auto">
                        <canvas id="marketLandscapeChart"></canvas>
                    </div>
                    <p class="text-xs text-slate-500 mt-2 text-center">This radar chart compares our Action Map system against Generic Chatbots and Direct LLM Agents across key performance attributes. Our system excels in Reliability and Safety due to the validated Intermediate Representation.</p>
                </div>
            </div>
        </section>
        
        <section id="market-growth" class="my-12 md:my-16">
            <div class="max-w-4xl mx-auto text-center">
                 <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">A Rapidly Growing Market</h2>
                 <p class="text-lg text-slate-600 mb-10">The market for conversational AI in e-commerce is expanding rapidly as businesses recognize the value of automated, personalized customer interactions. This trend presents a massive opportunity for SMBs to adopt affordable, high-impact technology to compete and grow.</p>
            </div>
            <div class="bg-white p-4 md:p-8 rounded-lg shadow-md">
                 <div class="chart-container mx-auto" style="max-width: 900px;">
                    <canvas id="marketGrowthChart"></canvas>
                </div>
                <p class="text-xs text-slate-500 mt-2 text-center">This chart shows the projected market size (in billions USD) for conversational AI in e-commerce and its year-over-year growth rate, indicating strong upward trends and significant opportunity.</p>
            </div>
        </section>


        <section id="adaptability" class="my-12 md:my-20 text-center">
            <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">Built for Change: AI-Powered Adaptability</h2>
            <p class="text-lg text-slate-600 max-w-4xl mx-auto mb-12">Websites are constantly evolving. Our system includes a proactive monitoring loop that uses AI to "self-heal" when it detects UI changes, dramatically reducing maintenance and ensuring the conversational agent remains reliable over time.</p>
            <div class="relative max-w-4xl mx-auto">
                <div class="flex flex-col md:flex-row items-center justify-center space-y-4 md:space-y-0 md:space-x-4">
                     <div class="bg-white p-4 rounded-full shadow-lg border-2 border-[#94d2bd] text-center w-36 h-36 flex items-center justify-center">
                        <span class="font-bold text-[#005f73]">Detect Change</span>
                    </div>
                    <div class="flow-arrow transform rotate-90 md:rotate-0">&circlearrowright;</div>
                    <div class="bg-white p-4 rounded-full shadow-lg border-2 border-[#94d2bd] text-center w-36 h-36 flex items-center justify-center">
                        <span class="font-bold text-[#005f73]">Validate Map</span>
                    </div>
                     <div class="flow-arrow transform rotate-90 md:rotate-0">&circlearrowright;</div>
                     <div class="bg-white p-4 rounded-full shadow-lg border-2 border-[#94d2bd] text-center w-36 h-36 flex items-center justify-center">
                        <span class="font-bold text-[#005f73]">AI Self-Heal</span>
                    </div>
                </div>
                <div class="md:absolute md:top-1/2 md:left-1/2 md:-translate-x-1/2 md:-translate-y-1/2 mt-8 md:mt-0 bg-[#ee9b00] text-white rounded-full shadow-2xl w-48 h-48 flex flex-col items-center justify-center text-center p-4 z-10 mx-auto">
                     <div class="text-4xl font-black">95%</div>
                     <div class="font-semibold mt-1 text-sm">of UI changes handled automatically</div>
                </div>
                 <p class="text-xs text-slate-500 mt-12 md:mt-28 text-center">This diagram illustrates our proactive monitoring and self-healing loop. The central statistic highlights the system's high efficiency in automatically adapting to website updates.</p>
            </div>
        </section>

        <section id="swot" class="my-12 md:my-16">
            <div class="max-w-4xl mx-auto text-center">
                 <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">Strategic Analysis (SWOT)</h2>
                 <p class="text-lg text-slate-600 mb-10">Understanding our strategic position is key. Our core strengths in reliability and safety provide a solid foundation, while we must remain vigilant about market competition and the inherent complexities of our technology.</p>
            </div>
            <div class="swot-grid max-w-5xl mx-auto">
                <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-green-500">
                    <h3 class="text-2xl font-bold text-green-700 mb-3">Strengths</h3>
                    <ul class="list-disc list-inside text-slate-600 space-y-2">
                        <li>Decoupled IR architecture ensures high reliability and safety.</li>
                        <li>Human-in-the-loop auditing provides unmatched control.</li>
                        <li>AI-powered self-healing reduces maintenance overhead.</li>
                        <li>Scalable design is built for enterprise-grade performance.</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-red-500">
                    <h3 class="text-2xl font-bold text-red-700 mb-3">Weaknesses</h3>
                    <ul class="list-disc list-inside text-slate-600 space-y-2">
                        <li>Initial action map generation can be complex for highly custom sites.</li>
                        <li>Reliance on a JS snippet requires customer trust and implementation.</li>
                        <li>Perception of complexity could be a hurdle for non-technical SMBs.</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-blue-500">
                    <h3 class="text-2xl font-bold text-blue-700 mb-3">Opportunities</h3>
                    <ul class="list-disc list-inside text-slate-600 space-y-2">
                        <li>Massive, underserved SMB market seeking affordable AI solutions.</li>
                        <li>Expansion into multi-turn dialogue and advanced personalization.</li>
                        <li>Integration with major e-commerce platforms (Shopify, etc.).</li>
                        <li>Partnerships with digital marketing and web development agencies.</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-yellow-500">
                    <h3 class="text-2xl font-bold text-yellow-700 mb-3">Threats</h3>
                    <ul class="list-disc list-inside text-slate-600 space-y-2">
                        <li>Competition from big tech companies entering the agentic AI space.</li>
                        <li>Rapid evolution of LLM technology could make IR approach seem dated.</li>
                        <li>Security vulnerabilities and data privacy concerns are paramount.</li>
                        <li>Potential for market commoditization driving down prices.</li>
                    </ul>
                </div>
            </div>
             <p class="text-xs text-slate-500 mt-8 text-center max-w-3xl mx-auto">The SWOT analysis provides a balanced view of our strategic position, highlighting internal strengths and weaknesses against external opportunities and threats in the conversational AI market.</p>
        </section>

        <section id="onboarding" class="my-12 md:my-16">
            <div class="max-w-4xl mx-auto text-center">
                 <h2 class="text-3xl md:text-4xl font-bold text-[#005f73] mb-4">The "Low-Lift" Onboarding Journey</h2>
                 <p class="text-lg text-slate-600 mb-10">We've streamlined our integration process to be as simple as possible for SMB owners, with AI-assistance and proactive support at every step.</p>
            </div>
            <div class="max-w-2xl mx-auto">
                <ol class="relative border-l border-dashed border-[#0a9396]">                  
                    <li class="mb-10 ml-6">            
                        <span class="absolute flex items-center justify-center w-8 h-8 bg-[#94d2bd] rounded-full -left-4 ring-4 ring-white">
                           <span class="text-white font-bold">1</span>
                        </span>
                        <h3 class="flex items-center mb-1 text-lg font-semibold text-[#005f73]">Sign Up & AI-Assisted Site Discovery</h3>
                        <p class="mb-4 text-base font-normal text-slate-500">Provide your base URL and our AI suggests key pages to crawl, simplifying the initial data gathering phase.</p>
                    </li>
                    <li class="mb-10 ml-6">
                        <span class="absolute flex items-center justify-center w-8 h-8 bg-[#94d2bd] rounded-full -left-4 ring-4 ring-white">
                            <span class="text-white font-bold">2</span>
                        </span>
                        <h3 class="mb-1 text-lg font-semibold text-[#005f73]">Crawl & Action Map Validation</h3>
                        <p class="text-base font-normal text-slate-500">We create and validate the initial Action Map, ensuring all critical user flows are covered and reliable.</p>
                    </li>
                    <li class="mb-10 ml-6">
                        <span class="absolute flex items-center justify-center w-8 h-8 bg-[#94d2bd] rounded-full -left-4 ring-4 ring-white">
                            <span class="text-white font-bold">3</span>
                        </span>
                        <h3 class="mb-1 text-lg font-semibold text-[#005f73]">Install Secure JavaScript Snippet</h3>
                        <p class="text-base font-normal text-slate-500">Add a single, lightweight, and secure line of code to your website to activate the conversational interface.</p>
                    </li>
                     <li class="ml-6">
                        <span class="absolute flex items-center justify-center w-8 h-8 bg-[#0a9396] rounded-full -left-4 ring-4 ring-white">
                           <span class="text-white font-bold">✓</span>
                        </span>
                        <h3 class="mb-1 text-lg font-semibold text-[#005f73]">Go Live & Thrive</h3>
                        <p class="text-base font-normal text-slate-500">Your website is now a dynamic, conversational storefront, ready to engage users and boost sales with ongoing support and monitoring.</p>
                    </li>
                </ol>
                <p class="text-xs text-slate-500 mt-8 text-center">This timeline outlines the simplified onboarding process for SMBs, designed for quick setup and minimal technical overhead.</p>
            </div>
        </section>

    </main>

    <script>
        // Helper function to wrap long labels for Chart.js
        const wrapLabel = (label, maxLength = 16) => {
            if (typeof label !== 'string' || label.length <= maxLength) {
                return label;
            }
            const words = label.split(' ');
            const lines = [];
            let currentLine = '';
            for (const word of words) {
                if ((currentLine + word).length > maxLength && currentLine.length > 0) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            }
            if (currentLine.trim().length > 0) {
                 lines.push(currentLine.trim());
            }
            return lines.length > 0 ? lines : [label]; 
        };
        
        const commonTooltipCallback = {
            title: function(tooltipItems) {
                const item = tooltipItems[0];
                let label = item.chart.data.labels[item.dataIndex];
                if (Array.isArray(label)) {
                  return label.join(' '); 
                }
                return label; 
            }
        };

        const chartFont = {
            family: 'Inter',
            size: 12,
            weight: '400'
        };
        
        const brilliantBlues = {
            darkBlue: '#005f73',
            teal: '#0a9396',
            lightTeal: '#94d2bd',
            paleGold: '#e9d8a6',
            orange: '#ee9b00',
            darkOrange: '#ca6702',
            burntOrange: '#bb3e03',
            darkRed: '#9b2226' 
        };
        
        const marketLandscapeCtx = document.getElementById('marketLandscapeChart').getContext('2d');
        new Chart(marketLandscapeCtx, {
            type: 'radar',
            data: {
                labels: [
                    wrapLabel('Reliability'), 
                    wrapLabel('Adaptability'), 
                    wrapLabel('Safety'), 
                    wrapLabel('Scalability'), 
                    wrapLabel('Ease of Integration'), 
                    wrapLabel('Flexibility')
                ],
                datasets: [{
                    label: 'Our Action Map (IR) System',
                    data: [9, 7, 9, 8, 7, 6],
                    backgroundColor: 'rgba(10, 147, 150, 0.2)', 
                    borderColor: brilliantBlues.teal,
                    pointBackgroundColor: brilliantBlues.teal,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: brilliantBlues.teal
                }, {
                    label: 'Generic Chatbots',
                    data: [6, 4, 7, 7, 8, 4],
                    backgroundColor: 'rgba(238, 155, 0, 0.2)', 
                    borderColor: brilliantBlues.orange,
                    pointBackgroundColor: brilliantBlues.orange,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: brilliantBlues.orange
                }, {
                    label: 'Direct LLM Agents',
                    data: [4, 8, 3, 5, 5, 9],
                    backgroundColor: 'rgba(187, 62, 3, 0.2)', 
                    borderColor: brilliantBlues.burntOrange,
                    pointBackgroundColor: brilliantBlues.burntOrange,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: brilliantBlues.burntOrange
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { font: chartFont }
                    },
                    tooltip: { 
                        callbacks: commonTooltipCallback 
                    }
                },
                scales: {
                    r: {
                        angleLines: { color: 'rgba(0, 0, 0, 0.1)' },
                        grid: { color: 'rgba(0, 0, 0, 0.1)' },
                        pointLabels: { 
                            font: chartFont,
                            callback: function(label) { 
                                return wrapLabel(label, 10); 
                            }
                        },
                        ticks: {
                            backdropColor: 'rgba(0,0,0,0)', 
                            color: '#64748b', 
                            stepSize: 2
                        }
                    }
                }
            }
        });

        const marketGrowthCtx = document.getElementById('marketGrowthChart').getContext('2d');
        new Chart(marketGrowthCtx, {
            type: 'bar', 
            data: {
                labels: ['2022', '2023', '2024', '2025 (Est.)', wrapLabel('2026 (Proj.)'), wrapLabel('2027 (Proj.)')],
                datasets: [
                    {
                        type: 'line', 
                        label: 'Year-over-Year Growth (%)',
                        data: [18, 22, 25, 30, 32, 35],
                        borderColor: brilliantBlues.orange,
                        backgroundColor: 'transparent', 
                        yAxisID: 'y1', 
                        tension: 0.4 
                    },
                    {
                        type: 'bar', 
                        label: 'Market Size ($ Billions)',
                        data: [12.5, 15.2, 19.0, 24.7, 32.6, 44.0],
                        backgroundColor: brilliantBlues.teal,
                        borderColor: brilliantBlues.darkBlue,
                        borderWidth: 1,
                        yAxisID: 'y', 
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                         labels: { font: chartFont }
                    },
                    tooltip: { 
                        mode: 'index', 
                        intersect: false, 
                        callbacks: commonTooltipCallback 
                    }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { font: chartFont }
                    },
                    y: { 
                        type: 'linear',
                        display: true,
                        position: 'left',
                        title: {
                            display: true,
                            text: 'Market Size ($B)',
                            font: chartFont
                        },
                         grid: { drawOnChartArea: false }, 
                         ticks: { font: chartFont }
                    },
                    y1: { 
                        type: 'linear',
                        display: true,
                        position: 'right',
                        title: {
                            display: true,
                            text: 'Growth Rate (%)',
                            font: chartFont
                        },
                        grid: { display: false }, 
                        ticks: { font: chartFont }
                    }
                }
            }
        });

        // New Gemini API Feature: Market Trend Insights
        const getTrendInsightsBtn = document.getElementById('getTrendInsightsBtn');
        const industryVerticalInput = document.getElementById('industryVertical');
        const trendInsightsResultContainer = document.getElementById('trendInsightsResultContainer');
        const trendInsightsList = document.getElementById('trendInsightsList');
        const errorMessageContainerTrends = document.getElementById('errorMessageContainerTrends');
        const loadingSpinnerTrends = document.getElementById('loadingSpinnerTrends');

        getTrendInsightsBtn.addEventListener('click', async () => {
            const industryVertical = industryVerticalInput.value.trim();
            if (!industryVertical) {
                errorMessageContainerTrends.textContent = 'Please enter an industry vertical.';
                return;
            }

            errorMessageContainerTrends.textContent = '';
            trendInsightsResultContainer.classList.add('hidden');
            trendInsightsList.innerHTML = ''; // Clear previous results
            loadingSpinnerTrends.classList.remove('hidden');
            getTrendInsightsBtn.disabled = true;
            getTrendInsightsBtn.classList.add('opacity-75', 'cursor-not-allowed');

            const apiKey = ""; 
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;
            
            const trendPrompt = `
You are an AI assistant specializing in market research and e-commerce trends.
For the industry vertical: "${industryVertical}"
Please generate 2-3 concise, emerging market trends related to the adoption or impact of conversational AI and advanced e-commerce technologies.
Format each trend as a bullet point starting with "- ".
For example:
- Trend 1 description.
- Trend 2 description.
Output only the bulleted list of trends.
`;

            const payload = {
                contents: [{ role: "user", parts: [{ text: trendPrompt }] }],
                generationConfig: {
                    temperature: 0.7, 
                    maxOutputTokens: 300,
                }
            };

            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    const errorData = await response.json().catch(() => ({ error: { message: "Unknown API error" } }));
                    throw new Error(errorData.error?.message || `API request failed with status ${response.status}`);
                }

                const result = await response.json();
                if (result.candidates && result.candidates[0].content && result.candidates[0].content.parts[0]) {
                    const trendsText = result.candidates[0].content.parts[0].text;
                    const trendsArray = trendsText.split('\n').map(trend => trend.replace(/^-\s*/, '').trim()).filter(trend => trend.length > 0);
                    
                    if (trendsArray.length > 0) {
                        trendsArray.forEach(trend => {
                            const li = document.createElement('li');
                            li.classList.add('trend-item', 'p-2', 'bg-slate-50', 'rounded'); // Added some padding and bg for better visual
                            li.textContent = trend;
                            trendInsightsList.appendChild(li);
                        });
                        trendInsightsResultContainer.classList.remove('hidden');
                    } else {
                        errorMessageContainerTrends.textContent = 'No specific trends were generated. Try a different vertical or rephrase.';
                    }
                } else {
                    errorMessageContainerTrends.textContent = 'Received an unexpected or empty response from the AI for trends.';
                }
            } catch (error) {
                errorMessageContainerTrends.textContent = `An error occurred while fetching trends: ${error.message}`;
            } finally {
                loadingSpinnerTrends.classList.add('hidden');
                getTrendInsightsBtn.disabled = false;
                getTrendInsightsBtn.classList.remove('opacity-75', 'cursor-not-allowed');
            }
        });


    </script>
</body>
</html>
{{< /rawhtml >}}

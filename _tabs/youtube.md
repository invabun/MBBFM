---
layout: page
title: YouTube
icon: fab fa-youtube
order: 2
---

<style>
  .yt-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
  }
  .yt-item {
    display: block; text-decoration: none; color: inherit;
    border-radius: 10px; overflow: hidden;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    transition: all 0.3s ease;
  }
  .yt-item:hover {
    background: rgba(255,255,255,0.06);
    border-color: rgba(255,255,255,0.12);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }
  .yt-item .thumb {
    position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden;
  }
  .yt-item img {
    width: 100%; height: 100%; object-fit: cover;
    transition: transform 0.3s ease;
  }
  .yt-item:hover img { transform: scale(1.05); }
  .yt-item .play-icon {
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 48px; height: 48px; border-radius: 50%;
    background: rgba(255,0,0,0.85);
    display: flex; align-items: center; justify-content: center;
    opacity: 0; transition: opacity 0.3s ease;
  }
  .yt-item:hover .play-icon { opacity: 1; }
  .yt-item .play-icon::after {
    content: ''; display: block;
    border-left: 16px solid white; border-top: 10px solid transparent;
    border-bottom: 10px solid transparent; margin-left: 3px;
  }
  .yt-item .info { padding: 12px 14px; }
  .yt-item .title { font-size: 0.85rem; font-weight: 600; line-height: 1.4; }
  .yt-item .meta {
    font-size: 0.7rem; opacity: 0.4; margin-top: 6px; font-family: monospace;
  }
  .yt-header {
    text-align: center; margin-bottom: 2rem;
  }
  .yt-header a {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 8px 20px; border-radius: 20px;
    background: rgba(255,0,0,0.12); border: 1px solid rgba(255,0,0,0.25);
    color: #ff4444; text-decoration: none; font-size: 0.82rem; font-weight: 600;
    transition: all 0.2s ease;
  }
  .yt-header a:hover { background: rgba(255,0,0,0.2); }
</style>

<div class="yt-header">
  <a href="https://www.youtube.com/@MBBFM" target="_blank" rel="noopener noreferrer">
    <i class="fab fa-youtube"></i> 订阅频道
  </a>
</div>

<div class="yt-grid">
{% for video in site.data.youtube %}
  <a class="yt-item" href="{{ video.url }}" target="_blank" rel="noopener noreferrer">
    <div class="thumb">
      <img src="{{ video.thumbnail }}" alt="{{ video.title }}" loading="lazy">
      <div class="play-icon"></div>
    </div>
    <div class="info">
      <div class="title">{{ video.title }}</div>
      <div class="meta">{{ video.date }} · {{ video.views }} views</div>
    </div>
  </a>
{% endfor %}
</div>

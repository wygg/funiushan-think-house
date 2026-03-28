import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeObsidian from 'starlight-theme-obsidian';

export default defineConfig({
	integrations: [
		starlight({
			plugins: [starlightThemeObsidian()],
			title: 'Momo伏牛山居造屋记',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/' }
			],
			sidebar: [
				{
					label: '🧭 导航塔 (Navigation)',
					items: [
						{ label: '项目哲学与技术声明', link: '/000-项目哲学' },
						{ label: '全周期施工导图', link: '/000-全周期施工导航' },
					]
				},
				{
					label: '🏗️ 建造实录 (00至09流水线)',
					autogenerate: { directory: '01-建造实录' }
				}
			],
		}),
	],
});

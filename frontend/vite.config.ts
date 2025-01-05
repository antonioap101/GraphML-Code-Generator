import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'


// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'), // Configura el alias @ a src
        },
    },
    server: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true,
                rewrite: (path) => {
                    const rewrittenPath = path.replace(/^\/api/, '');
                    console.log('Original path:', path);
                    console.log('Rewritten path:', rewrittenPath);

                    return rewrittenPath;
                }

            }
        },
    }
});
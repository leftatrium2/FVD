/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_BASE_API: string
  readonly VITE_APP_ENV: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module '*.css' {
  const content: { [className: string]: string }
  export default content
}

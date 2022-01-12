# playground-vue3

[Vite guide](https://vitejs.dev/guide/#scaffolding-your-first-vite-project)

## Install

```zsh
$npm init vite@latest

Need to install the following packages:
  create-vite@latest
Ok to proceed? (y) y
✔ Project name: … sample-project
✔ Select a framework: › vue
✔ Select a variant: › vue-ts

Scaffolding project in /hogehoge/git/playground-vue3/sample-project...

Done. Now run:

  cd sample-project
  npm install
  npm run dev

$cd sample-project
$npm install
$npm run dev

> sample-project@0.0.0 dev
> vite

Pre-bundling dependencies:
  vue
(this will be run only when your dependencies or config have changed)

  vite v2.7.10 dev server running at:

  > Local: http://localhost:3000/
  > Network: use `--host` to expose

  ready in 361ms.

```

Go to [http://localhost:3000/](http://localhost:3000/):

## For VSCode Setting

Install `johnsoncodehk.volar` instead `vuter`.  
And I'd better check VSCode setting `Volar: Switch TS Plugin on/off` to be enable Volar's `.vue` type support plugin. But I can't find it then I'll check again later.  
(I think it already works because `Project/tsconfig.json` has `include` setting, and it include `src/**/*.vue`, I'm not sure.)

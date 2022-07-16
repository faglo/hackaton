eslint-disable 
module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: "@babel/eslint-parser",
    requireConfigFile: false,
  },
  extends: ["@nuxtjs", "plugin:nuxt/recommended"],
  plugins: [],
  // add your custom rules here
  rules: {
    skipBlankLines: true,
    "space-before-function-paren": ["never"],
    "vue/multi-word-component-names": ["error", {
      "ignores": []
    }],
    "eol-last": "never"
  },
};

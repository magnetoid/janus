const { contextBridge, ipcRenderer, webUtils } = require('electron')

contextBridge.exposeInMainWorld('janusDesktop', {
  getConnection: profile => ipcRenderer.invoke('janus:connection', profile),
  touchBackend: profile => ipcRenderer.invoke('janus:backend:touch', profile),
  getGatewayWsUrl: profile => ipcRenderer.invoke('janus:gateway:ws-url', profile),
  getBootProgress: () => ipcRenderer.invoke('janus:boot-progress:get'),
  getConnectionConfig: profile => ipcRenderer.invoke('janus:connection-config:get', profile),
  saveConnectionConfig: payload => ipcRenderer.invoke('janus:connection-config:save', payload),
  applyConnectionConfig: payload => ipcRenderer.invoke('janus:connection-config:apply', payload),
  testConnectionConfig: payload => ipcRenderer.invoke('janus:connection-config:test', payload),
  probeConnectionConfig: remoteUrl => ipcRenderer.invoke('janus:connection-config:probe', remoteUrl),
  oauthLoginConnectionConfig: remoteUrl => ipcRenderer.invoke('janus:connection-config:oauth-login', remoteUrl),
  oauthLogoutConnectionConfig: remoteUrl => ipcRenderer.invoke('janus:connection-config:oauth-logout', remoteUrl),
  profile: {
    get: () => ipcRenderer.invoke('janus:profile:get'),
    set: name => ipcRenderer.invoke('janus:profile:set', name)
  },
  api: request => ipcRenderer.invoke('janus:api', request),
  notify: payload => ipcRenderer.invoke('janus:notify', payload),
  requestMicrophoneAccess: () => ipcRenderer.invoke('janus:requestMicrophoneAccess'),
  readFileDataUrl: filePath => ipcRenderer.invoke('janus:readFileDataUrl', filePath),
  readFileText: filePath => ipcRenderer.invoke('janus:readFileText', filePath),
  selectPaths: options => ipcRenderer.invoke('janus:selectPaths', options),
  writeClipboard: text => ipcRenderer.invoke('janus:writeClipboard', text),
  saveImageFromUrl: url => ipcRenderer.invoke('janus:saveImageFromUrl', url),
  saveImageBuffer: (data, ext) => ipcRenderer.invoke('janus:saveImageBuffer', { data, ext }),
  saveClipboardImage: () => ipcRenderer.invoke('janus:saveClipboardImage'),
  getPathForFile: file => {
    try {
      return webUtils.getPathForFile(file) || ''
    } catch {
      return ''
    }
  },
  normalizePreviewTarget: (target, baseDir) => ipcRenderer.invoke('janus:normalizePreviewTarget', target, baseDir),
  watchPreviewFile: url => ipcRenderer.invoke('janus:watchPreviewFile', url),
  stopPreviewFileWatch: id => ipcRenderer.invoke('janus:stopPreviewFileWatch', id),
  setTitleBarTheme: payload => ipcRenderer.send('janus:titlebar-theme', payload),
  setPreviewShortcutActive: active => ipcRenderer.send('janus:previewShortcutActive', Boolean(active)),
  openExternal: url => ipcRenderer.invoke('janus:openExternal', url),
  fetchLinkTitle: url => ipcRenderer.invoke('janus:fetchLinkTitle', url),
  settings: {
    getDefaultProjectDir: () => ipcRenderer.invoke('janus:setting:defaultProjectDir:get'),
    setDefaultProjectDir: dir => ipcRenderer.invoke('janus:setting:defaultProjectDir:set', dir),
    pickDefaultProjectDir: () => ipcRenderer.invoke('janus:setting:defaultProjectDir:pick')
  },
  revealLogs: () => ipcRenderer.invoke('janus:logs:reveal'),
  getRecentLogs: () => ipcRenderer.invoke('janus:logs:recent'),
  readDir: dirPath => ipcRenderer.invoke('janus:fs:readDir', dirPath),
  gitRoot: startPath => ipcRenderer.invoke('janus:fs:gitRoot', startPath),
  terminal: {
    dispose: id => ipcRenderer.invoke('janus:terminal:dispose', id),
    resize: (id, size) => ipcRenderer.invoke('janus:terminal:resize', id, size),
    start: options => ipcRenderer.invoke('janus:terminal:start', options),
    write: (id, data) => ipcRenderer.invoke('janus:terminal:write', id, data),
    onData: (id, callback) => {
      const channel = `janus:terminal:${id}:data`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)
      return () => ipcRenderer.removeListener(channel, listener)
    },
    onExit: (id, callback) => {
      const channel = `janus:terminal:${id}:exit`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)
      return () => ipcRenderer.removeListener(channel, listener)
    }
  },
  onClosePreviewRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('janus:close-preview-requested', listener)
    return () => ipcRenderer.removeListener('janus:close-preview-requested', listener)
  },
  onOpenUpdatesRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('janus:open-updates', listener)
    return () => ipcRenderer.removeListener('janus:open-updates', listener)
  },
  onWindowStateChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('janus:window-state-changed', listener)
    return () => ipcRenderer.removeListener('janus:window-state-changed', listener)
  },
  onPreviewFileChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('janus:preview-file-changed', listener)
    return () => ipcRenderer.removeListener('janus:preview-file-changed', listener)
  },
  onBackendExit: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('janus:backend-exit', listener)
    return () => ipcRenderer.removeListener('janus:backend-exit', listener)
  },
  onPowerResume: callback => {
    const listener = () => callback()
    ipcRenderer.on('janus:power-resume', listener)
    return () => ipcRenderer.removeListener('janus:power-resume', listener)
  },
  onBootProgress: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('janus:boot-progress', listener)
    return () => ipcRenderer.removeListener('janus:boot-progress', listener)
  },
  // First-launch bootstrap progress -- emitted by the install.ps1 stage
  // runner in main.cjs (apps/desktop/electron/bootstrap-runner.cjs).
  // Renderer's install overlay subscribes to live events and queries the
  // current snapshot via getBootstrapState() to recover after a devtools
  // reload mid-bootstrap.
  getBootstrapState: () => ipcRenderer.invoke('janus:bootstrap:get'),
  resetBootstrap: () => ipcRenderer.invoke('janus:bootstrap:reset'),
  repairBootstrap: () => ipcRenderer.invoke('janus:bootstrap:repair'),
  cancelBootstrap: () => ipcRenderer.invoke('janus:bootstrap:cancel'),
  onBootstrapEvent: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('janus:bootstrap:event', listener)
    return () => ipcRenderer.removeListener('janus:bootstrap:event', listener)
  },
  getVersion: () => ipcRenderer.invoke('janus:version'),
  uninstall: {
    summary: () => ipcRenderer.invoke('janus:uninstall:summary'),
    run: mode => ipcRenderer.invoke('janus:uninstall:run', { mode })
  },
  updates: {
    check: () => ipcRenderer.invoke('janus:updates:check'),
    apply: opts => ipcRenderer.invoke('janus:updates:apply', opts),
    getBranch: () => ipcRenderer.invoke('janus:updates:branch:get'),
    setBranch: name => ipcRenderer.invoke('janus:updates:branch:set', name),
    onProgress: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('janus:updates:progress', listener)
      return () => ipcRenderer.removeListener('janus:updates:progress', listener)
    }
  }
})

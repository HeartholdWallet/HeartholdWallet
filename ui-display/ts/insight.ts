

type WalletInteraction = {
    source: string
    target: string
    weight: number
    timestamp: number
}

type ClusterProfile = {
    clusterId: number
    members: string[]
    centrality: number
    suspiciousScore: number
}
